require("perf_hooks");var e="​",n={leftToRightMark:"‎",rightToLeftMark:"‏",zeroWidthNonJoiner:"‌",zeroWidthJoiner:"‍",zeroWidthNoBreakSpace:"\ufeff",zeroWidthSpace:e},l=Object.keys(n).map(function(r){return n[r]}),g=l.reduce(function(r,t,e){return r[t]=""+e,r},{});function h(r){for(var t="",n=0;n<r.length;n++){for(var o=r.codePointAt(n),i=o.toString(5),f="",h=0;h<i.length;h++)f+=l[+i.charAt(h)];t+=(n=o<65536?n:n+1)===r.length-1?f:f+e}return t}function a(r){var t="";if(0===r.length)return t;for(var n=r.split(e),o=0;o<n.length;o++){for(var i="",f=0;f<n[o].length;f++)i+=g[n[o].charAt(f)];t+=String.fromCodePoint(parseInt(i,5))}return t}function c(r){for(var t="",e="",n=0,o=r;n<o.length;n+=1){var i=o[n];g[i]?e+=i:t+=i}return{vis:t,hid:e}}exports.zeroWidthDict=n,exports.t2z=h,exports.z2t=a,exports.encode=function(r,t){var e="",n=h(t);if(0===r.length)return n;for(var o=!1,i=0,f=r;i<f.length;i+=1)e+=f[i],o||(e+=n,o=!0);return e},exports.extract=c,exports.decode=function(r){return a(c(r).hid)},exports.split=function(r){for(var t="",n=0,o=r;n<o.length;n+=1)t+=o[n],t+=e;return t};
//# sourceMappingURL=zero-width-lib.js.map
