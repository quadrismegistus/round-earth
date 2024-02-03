from .imports import *

geoloc_js = """
/*! For license information please see set-interval-async.iife.js.LICENSE.txt */

var SetIntervalAsync;(()=>{var e={912:e=>{e.exports=function(e,t){return t.get?t.get.call(e):t.value},e.exports.__esModule=!0,e.exports.default=e.exports},448:e=>{e.exports=function(e,t,r){if(t.set)t.set.call(e,r);else{if(!t.writable)throw new TypeError("attempted to set read only private field");t.value=r}},e.exports.__esModule=!0,e.exports.default=e.exports},69:e=>{e.exports=function(e,t,r){if(!t.has(e))throw new TypeError("attempted to "+r+" private field on non-instance");return t.get(e)},e.exports.__esModule=!0,e.exports.default=e.exports},468:(e,t,r)=>{var n=r(912),a=r(69);e.exports=function(e,t){var r=a(e,t,"get");return n(e,r)},e.exports.__esModule=!0,e.exports.default=e.exports},661:(e,t,r)=>{var n=r(448),a=r(69);e.exports=function(e,t,r){var s=a(e,t,"set");return n(e,s,r),r},e.exports.__esModule=!0,e.exports.default=e.exports},836:e=>{e.exports=function(e){return e&&e.__esModule?e:{default:e}},e.exports.__esModule=!0,e.exports.default=e.exports},874:(e,t,r)=>{"use strict";Object.defineProperty(t,"__esModule",{value:!0}),t.clearIntervalAsync=void 0;const n=r(572);t.clearIntervalAsync=async function(e){if(!(e instanceof n.SetIntervalAsyncTimer))throw new TypeError("First argument is not an instance of SetIntervalAsyncTimer");await n.SetIntervalAsyncTimer.stopTimer(e)}},653:(e,t,r)=>{"use strict";Object.defineProperty(t,"__esModule",{value:!0}),t.setIntervalAsync=t.clearIntervalAsync=void 0;const n=r(874);Object.defineProperty(t,"clearIntervalAsync",{enumerable:!0,get:function(){return n.clearIntervalAsync}});const a=r(572);t.setIntervalAsync=function(e,t){if("function"!=typeof e)throw new TypeError("First argument is not a function");if("number"!=typeof t)throw new TypeError("Second argument is not a number");for(var r=arguments.length,n=new Array(r>2?r-2:0),s=2;s<r;s++)n[s-2]=arguments[s];return a.SetIntervalAsyncTimer.startTimer("dynamic",e,t,...n)}},670:(e,t,r)=>{"use strict";Object.defineProperty(t,"__esModule",{value:!0}),t.setIntervalAsync=t.clearIntervalAsync=void 0;const n=r(874);Object.defineProperty(t,"clearIntervalAsync",{enumerable:!0,get:function(){return n.clearIntervalAsync}});const a=r(572);t.setIntervalAsync=function(e,t){if("function"!=typeof e)throw new TypeError("First argument is not a function");if("number"!=typeof t)throw new TypeError("Second argument is not a number");for(var r=arguments.length,n=new Array(r>2?r-2:0),s=2;s<r;s++)n[s-2]=arguments[s];return a.SetIntervalAsyncTimer.startTimer("fixed",e,t,...n)}},572:(e,t,r)=>{"use strict";var n=r(836),a=n(r(468)),s=n(r(661));function o(e,t){c(e,t),t.add(e)}function i(e,t,r){c(e,t),t.set(e,r)}function c(e,t){if(t.has(e))throw new TypeError("Cannot initialize the same private elements twice on an object")}function l(e,t,r){if(!t.has(e))throw new TypeError("attempted to get private field on non-instance");return r}Object.defineProperty(t,"__esModule",{value:!0}),t.SetIntervalAsyncTimer=void 0;var u=new WeakMap,f=new WeakMap,v=new WeakMap,y=new WeakSet,d=new WeakSet;class p{constructor(){o(this,d),o(this,y),i(this,u,{writable:!0,value:void 0}),i(this,f,{writable:!0,value:void 0}),i(this,v,{writable:!0,value:!1})}static startTimer(e,t,r){r=Math.min(Math.max(Math.trunc(r),10),2147483647);const n=new p;for(var a=arguments.length,s=new Array(a>3?a-3:0),o=3;o<a;o++)s[o-3]=arguments[o];return l(n,y,w).call(n,e,t,r,r,...s),n}static async stopTimer(e){(0,s.default)(e,v,!0),(0,a.default)(e,u)&&clearTimeout((0,a.default)(e,u)),(0,a.default)(e,f)&&await(0,a.default)(e,f)}}function w(e,t,r,n){for(var o=arguments.length,i=new Array(o>4?o-4:0),c=4;c<o;c++)i[c-4]=arguments[c];(0,s.default)(this,u,setTimeout((async()=>{(0,s.default)(this,u,void 0),(0,s.default)(this,f,l(this,d,m).call(this,e,t,r,...i)),await(0,a.default)(this,f),(0,s.default)(this,f,void 0)}),n))}async function m(e,t,r){const n=(new Date).getTime();for(var s=arguments.length,o=new Array(s>3?s-3:0),i=3;i<s;i++)o[i-3]=arguments[i];try{await t(...o)}finally{if(!(0,a.default)(this,v)){const a=(new Date).getTime()-n,s="dynamic"===e?r>a?r-a:0:r;l(this,y,w).call(this,e,t,r,s,...o)}}}t.SetIntervalAsyncTimer=p}},t={};function r(n){var a=t[n];if(void 0!==a)return a.exports;var s=t[n]={exports:{}};return e[n](s,s.exports,r),s.exports}var n={};(()=>{"use strict";var e=n;Object.defineProperty(e,"__esModule",{value:!0}),e.fixed=e.dynamic=e.clearIntervalAsync=e.setIntervalAsync=void 0;const t=r(874);Object.defineProperty(e,"clearIntervalAsync",{enumerable:!0,get:function(){return t.clearIntervalAsync}});const a=r(653),s=r(670),o=a.setIntervalAsync;e.setIntervalAsync=o;const i={setIntervalAsync:a.setIntervalAsync};e.dynamic=i;const c={setIntervalAsync:s.setIntervalAsync};e.fixed=c})(),SetIntervalAsync=n})();
var setIntervalAsync = SetIntervalAsync.setIntervalAsync;


window.geoloc = {'lat':0.0, 'lon':0.0};
window.geolocated = 0;

watcher = setIntervalAsync(
    async () => {
        if(!window.geolocated) { 
            await navigator.geolocation.getCurrentPosition(
                (pos) => { 
                    window.geoloc = {
                        'lat':pos.coords.latitude,
                        'lon':pos.coords.longitude
                    };
                    window.geolocated = 1;
                }
            );
        }
    },
    500
);



"""

hover_js = """

window.hover_json = "";
window.hover_key = "";
setInterval(
    function() {
        const els = window.document.getElementsByClassName('hoverlayer');
        if(els.length) {
            const el = els[0];
            const txt = el.textContent;
            if(txt!=window.hover_json) {
                window.hover_json = txt;
                window.hover_key = "";
            }
        }
    },
    100
);

window.mouseX = 0;
window.mouseY = 0;

function updateMouseLoc(event) {
    window.mouseX = event.clientX;
    window.mouseY = event.clientY;
}

document.addEventListener('mousemove', updateMouseLoc);
document.body.style.overflow = 'hidden';

var style = document.createElement('style');
style.innerHTML = `
  a:hover { 
    text-decoration: none !important; 
  }
`;
document.head.appendChild(style);

window.systemColorScheme = '';

window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', event => {
    window.systemColorScheme = event.matches ? "dark" : "light";
});

document.addEventListener('keydown', function(event) {
    const key = event.key; // "a", "1", "Shift", etc.
    if(key=="d") {
        window.hover_key=key;
    }
});

"""
