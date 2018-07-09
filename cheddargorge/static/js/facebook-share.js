window.fbAsyncInit = function() {
  FB.init({
    appId: '308313999705638',
    autoLogAppEvents: true,
    xfbml: true,
    version: 'v3.0'
  });
};

(function(d, s, id) {
  var js, fjs = d.getElementsByTagName(s)[0];
  if (d.getElementById(id)) { return; }
  js = d.createElement(s); js.id = id;
  js.src = "https://connect.facebook.net/en_US/sdk.js";
  fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));

document.getElementById('fbShare').onclick = function() {
  FB.ui({
    method: 'share',
    display: 'popup',
    href: 'https://www.cheddargorge.fun',
    quote: 'Your friend just added a word to the latest story on Cheddar Gorge. Sign up or login now to add the next word...'
  }, function(response) { });
};
