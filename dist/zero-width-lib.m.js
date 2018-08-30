var zeroWidthNonJoiner="‌",zeroWidthJoiner="‍",zeroWidthSpace="​",zeroWidthNoBreakSpace="\ufeff",leftToRightMark="‎",rightToLeftMark="‏",zeroWidthDict={leftToRightMark:leftToRightMark,rightToLeftMark:rightToLeftMark,zeroWidthNonJoiner:zeroWidthNonJoiner,zeroWidthJoiner:zeroWidthJoiner,zeroWidthNoBreakSpace:zeroWidthNoBreakSpace,zeroWidthSpace:zeroWidthSpace},Quinary2ZeroMap=Object.keys(zeroWidthDict).map(function(r){return zeroWidthDict[r]}),Zero2QuinaryMap=Quinary2ZeroMap.reduce(function(r,t,e){return r[t]=""+e,r},{});function t2z(r){for(var t="",e=0;e<r.length;e++){for(var o=r.codePointAt(e),i=o.toString(5),n="",a=0;a<i.length;a++)n+=Quinary2ZeroMap[+i.charAt(a)];t+=(e=o<65536?e:e+1)===r.length-1?n:n+zeroWidthSpace}return t}function z2t(r){var t="";if(0===r.length)return t;for(var e=r.split(zeroWidthSpace),o=0;o<e.length;o++){for(var i="",n=0;n<e[o].length;n++)i+=Zero2QuinaryMap[e[o].charAt(n)];t+=String.fromCodePoint(parseInt(i,5))}return t}function encode(r,t){var e="",o=t2z(t);if(0===r.length)return o;var i=!1,n=!0,a=!1,h=void 0;try{for(var c,u=r[Symbol.iterator]();!(n=(c=u.next()).done);n=!0){e+=c.value,i||(e+=o,i=!0)}}catch(r){a=!0,h=r}finally{try{n||null==u.return||u.return()}finally{if(a)throw h}}return e}function extract(r){var t="",e="",o=!0,i=!1,n=void 0;try{for(var a,h=r[Symbol.iterator]();!(o=(a=h.next()).done);o=!0){var c=a.value;Zero2QuinaryMap[c]?e+=c:t+=c}}catch(r){i=!0,n=r}finally{try{o||null==h.return||h.return()}finally{if(i)throw n}}return{vis:t,hid:e}}function decode(r){return z2t(extract(r).hid)}function split(r){var t="",e=!0,o=!1,i=void 0;try{for(var n,a=r[Symbol.iterator]();!(e=(n=a.next()).done);e=!0){t+=n.value,t+=zeroWidthSpace}}catch(r){o=!0,i=r}finally{try{e||null==a.return||a.return()}finally{if(o)throw i}}return t}export{zeroWidthDict,t2z,z2t,encode,extract,decode,split};
