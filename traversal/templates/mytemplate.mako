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
      <div class="align-left">
	<p>Userid: ${request.user}
	% if request.user:
	    <a href="/logout">Logout</a>
	% else:
	    <a href="/login">Login</a>
	% endif
	</p>
      </div>
      <div class="top-small align-center">
        <div>
	    <img width="220" height="50" alt="pyramid" src="${request.static_url('traversal:static/pyramid-small.png')}" />
	</div>
      </div>
    </div>
    <div id="middle">
      <div class="align-left">
	View: ${view}
	<h2>${request.context}</h2>
	% if request.context.has_permission('edit'):
	  <a href="edit">Edit</a>
	% endif
      </div>
    </div>
    <div id="bottom">
      <table>
	<tr>
	  <td>${' . '.join([u'<a href="%s">%s</a>' % (request.resource_url(resource), resource) for resource in request.context.lineage()]) | n}</td>
	  <td>
	    <ul>
	      ${' '.join(['<li><a href="%s" class="%s">%s</a></li>' % (request.resource_url(child), 'forbidden' if not child.has_permission('view') else '', child) for child in request.context.children() ] ) | n}
	    </ul>
	  </td>
	</tr>
      </table>
    </div>
  </div>
  <div id="footer">
  </div>
</body>
</html>
