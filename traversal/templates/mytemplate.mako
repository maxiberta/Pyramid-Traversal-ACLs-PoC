<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" xmlns:tal="http://xml.zope.org/namespaces/tal">
<head>
  <title>SmD - User Permissions PoC</title>
  <meta http-equiv="Content-Type" content="text/html;charset=UTF-8"/>
  <link rel="shortcut icon" href="${request.static_url('traversal:static/favicon.ico')}" />
  <link rel="stylesheet" href="${request.static_url('traversal:static/pylons.css')}" type="text/css" media="screen" charset="utf-8" />
</head>
<body>
  <div id="wrap">
    <div id="top-small">
      <div class="top-small align-center">
        <div>
	    <img width="220" height="50" alt="pyramid" src="${request.static_url('traversal:static/pyramid-small.png')}" />
	</div>
      </div>
    </div>
    <div id="middle">
      <div class="middle align-center">
	<h1>Userid: ${userid or 'None'}</h1>
	% if userid:
	    <a href="/logout">Logout</a>
	% else:
	    <a href="/login">Login</a>
	% endif
      </div>
    </div>
    <div id="bottom">
      <div class="bottom">
        <div id="left" class="align-right">
        </div>
        <div id="right" class="align-left">
        </div>
      </div>
    </div>
  </div>
  <div id="footer">
  </div>
</body>
</html>
