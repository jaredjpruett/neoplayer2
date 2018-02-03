// ==UserScript==
// @name            SearchIdentical
// @namespace       https://github.com/zmnmxlntr
// @include         http://www.neopets.com/market.phtml?type=wizard
// @include         http://www.neopets.com/island/tradingpost.phtml?type=browse
// @version         2.0
// @grant           none
// ==/UserScript==

if(document.URL === "http://www.neopets.com/market.phtml?type=wizard") {
    document.getElementsByName('criteria')[0].value = "exact";
} else if(document.URL === "http://www.neopets.com/island/tradingpost.phtml?type=browse") {
    document.getElementsByName('criteria')[0].value = "item_exact";
    document.getElementById('tp_newest').checked = true;
}
