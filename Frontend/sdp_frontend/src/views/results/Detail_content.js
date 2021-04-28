export const xss_description = `This script is possibly vulnerable to Cross Site Scripting (XSS) attacks. 
Cross site scripting (also referred to as XSS) is a vulnerability that allows an attacker to send malicious code (usually in the form of Javascript) to another user. 
Because a browser cannot know if the script should be trusted or not, it will execute the script in the user context allowing the attacker to access any cookies or session tokens retained by the browser.`;

export const sql_description = `A SQL injection attack consists of insertion or “injection” of a SQL query via the input data from the client to the application. 
A successful SQL injection exploit can read sensitive data from the database, modify database data (Insert/Update/Delete), execute administration operations on the database 
(such as shutdown the DBMS), recover the content of a given file present on the DBMS file system and in some cases issue commands to the operating system. SQL injection attacks 
are a type of injection attack, in which SQL commands are injected into data-plane input in order to affect the execution of predefined SQL commands.`;

export const xss_impact = `Malicious users may inject JavaScript, VBScript, ActiveX, HTML or Flash into a vulnerable application to fool a user in order to gather data from them. 
An attacker can steal the session cookie and take over the account, impersonating the user. It is also possible to modify the content of the page presented to the user.`;

export const sql_impact = `The impact SQL injection can have on a business is far-reaching.
A successful attack may result in the unauthorized viewing of user lists, the deletion of entire tables and, in certain cases, 
the attacker gaining administrative rights to a database, all of which are highly detrimental to a business.`;

export const xss_fix = `Your script should filter metacharacters from user input.`;

export const sql_fix = `The only sure way to prevent SQL Injection attacks is input validation and parametrized queries including prepared statements. 
The application code should never use the input directly. The developer must sanitize all input, not only web form inputs such as login forms. 
They must remove potential malicious code elements such as single quotes. It is also a good idea to turn off the visibility of database errors on your production sites. 
Database errors can be used with SQL Injection to gain information about your database.`;

export const xss_web_reference = [
  {
    name: "The Cross Site Scripting Faq",
    link: "http://www.cgisecurity.com/xss-faq.html",
  },
  {
    name: "OWASP Cross Site Scripting",
    link: "http://www.owasp.org/index.php/Cross_Site_Scripting",
  },
  {
    name: "XSS Filter Evasion Cheat Sheet",
    link: "https://www.owasp.org/index.php/XSS_Filter_Evasion_Cheat_Sheet",
  },
  {
    name: "Cross site scripting",
    link: "http://en.wikipedia.org/wiki/Cross-site_scripting",
  },
  { name: "OWASP Top Ten", link: "https://owasp.org/www-project-top-ten/" },
  {
    name: "How To: Prevent Cross-Site Scripting in ASP.NET",
    link: "http://msdn.microsoft.com/en-us/library/ms998274.aspx",
  },
];

export const sql_web_reference = [
  {
    name: "The SQL Injection Faq",
    link: "https://www.sqlsecurity.com/faqs-1/sql-injection-faq",
  },
  {
    name: "OWASP SQL Injection",
    link: "https://owasp.org/www-community/attacks/SQL_Injection",
  },
  {
    name: "SQL Injection",
    link: "https://en.wikipedia.org/wiki/SQL_injection",
  },
  { name: "OWASP Top Ten", link: "https://owasp.org/www-project-top-ten/" },
];
