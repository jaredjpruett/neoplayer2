// ==UserScript==
// @name            BankConfirmer
// @description     Suppresses Javascript's 'unsafe window' box.
// @include         http://www.neopets.com/bank.phtml
// @version         2.0
// @grant           none
// ==/UserScript==

unsafeWindow.confirm = function() { return true; };
