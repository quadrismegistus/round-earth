from .base import *

class Place(Base):
    __tablename__ = 'place'
    id: Mapped[int] = mapped_column(primary_key=True)
    point = Column(Geometry(geometry_type='POINT', srid=4326))
    name: Mapped[str]

    type: Mapped[Optional[str]]
    country: Mapped[Optional[str]] = mapped_column(String(2))

    @classmethod
    def nearby(cls, lat, lon, mindist_km=None):
        point = get_point(lat, lon)
        for place in get_db_session().query(cls).order_by(
                func.ST_Distance(
                    cls.point,
                    point,
                )):
            dist = place.dist_from(lat, lon)
            if not np.isnan(dist):
                if mindist_km and dist > mindist_km: break
                yield place, dist

    @classmethod
    def located_at(cls, lat=None, lon=None, ip=None, mindist_km=10):
        if not lat or not lon:
            lat,lon = geo_ip(ip)
        if not lat or not lon:
            return
        places = cls.nearest(lat,lon,mindist_km=mindist_km)
        if places: 
            place = places[0][0]
        else:
            place = Place(**geodecode(lat,lon)).save()
        return place
    
    @classmethod
    def located_here(cls):
        return cls.located_at()

    def dist_from(self, lat, lon, metric='km'):
        try:
            dist = geodesic((lat, lon), (self.lat, self.lon))
            return getattr(dist, metric)
        except ValueError as e:
            print(e)
            return np.nan

    @cached_property
    def latlon(self):
        point = wkb.loads(self.point.data.tobytes())
        return (point.y, point.x)

    @property
    def lat(self):
        return self.latlon[0]

    @property
    def lon(self):
        return self.latlon[1]

    @cached_property
    def point_str(self):
        return f'POINT({self.lon} {self.lat})'

    def __repr__(self):
        return f'Place(id={self.id}, name={self.name}, point="{self.point_str}")'

