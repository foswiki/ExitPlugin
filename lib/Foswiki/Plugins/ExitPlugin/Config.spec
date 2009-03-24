# ---+ Plugins
# ---++ Exitlugin
# This plugin redirects links to external sites via a page of your choice.
# You might want to do that to display a disclaimer
# ("You are leaving foswiki.org, come back soon.")
# or to remove topic names from HTTP referer headers.

# **PERL**
# An array of strings listing the URI schemes to be redirected
$Foswiki::cfg{Plugins}{ExitPlugin}{Schemes} = ['http', 'https'];

# **URL 80**
# Exit handler
$Foswiki::cfg{Plugins}{ExitPlugin}{RedirectVia} = '%SCRIPTURL%/rest/ExitPlugin/exit?url=';

# **PERL**
# An array of strings listing the hosts for which no exit page should be shown.
$Foswiki::cfg{Plugins}{ExitPlugin}{NoExit} = ['.twiki.org', '.foswiki.org'];

# **STRING 30*
# External link marks (you can use an image if you want). These are optional.
#$Foswiki::cfgg{Plugins}{ExitPlugin}{Premark} = '';
#$Foswiki::cfgg{Plugins}{ExitPlugin}{Postmark} = '';

# **BOOLEAN**
# Include the external link marks withing the HREF tag.
$Foswiki::cfg{Plugins}{ExitPlugin}{MarksInLink} = 0;

# **BOOLEAN**
# Debug flag
$Foswiki::cfg{Plugins}{ExitPlugin}{Debug} = 0;

1;