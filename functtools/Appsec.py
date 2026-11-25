# class GamePlayer:
#     health: list[str] = ["apple"]  # Is this a class attribute or an instance attribute?
# # behaves totally differently for mutables and immutables. 
# p1 = GamePlayer()
# p2 = GamePlayer()
# p1.health.append("carrot")
# print(p2.health)  # What prints out, and why do people get burned by this?
# print(p1.health)


# # class UserSession:
# #     # Role permissions shared across the application session
# #     permissions = ["read"]

# #     def __init__(self, username: str, is_admin: bool = False):
# #         self.username = username
# #         self.is_admin = is_admin
# #         if self.is_admin:
# #             self.permissions.append("write")
# #             self.permissions.append("execute")

# #     def get_permissions(self):
# #         return list(self.permissions)


# # session = UserSession("Taofeek", True)
# # session.is_admin = True
# # # type(session).__init__(session, "Taofeek", True) # reinitialization
# # print(session.get_permissions())


# # session_2 = UserSession("Taiwo")
# # print(session_2.get_permissions())

# # permissions = session_2.permissions
# # permissions.append("delete")
# # print(session_2.get_permissions())

# class Game_Player_2:
#     health = 50
    
# # p3 = Game_Player_2()
# # p4 = Game_Player_2()
# # p4.health += 23 # This is where descriptors and __new__ comes in.
# # print(p3.health)
# # print(p4.health) 

# # build programs that don't allow decorators over them, check for system versions, and rule out unofficial installations. 


# class UserSession:
#     # Role permissions shared across the application session
#     permissions = ["read"]

#     def __init__(self, username: str, is_admin: bool = False):
#         self.username = username
#         self.is_admin = is_admin
#         if self.is_admin:
#             self.permissions.append("write")
#             self.permissions.append("execute")

#     def get_permissions(self):
#         return self.permissions
    
# user = UserSession("Taofeek")
# print(user.permissions)

# user_2 = UserSession("Taiwo", True)
# # print(user.permissions)
# # print(user.permissions)

# # Copy.copy on a flat list creates a brand new list object in RAM.


"""
Flaw 1: The Mutable Default Argument Trap (State Leakage)

The Antipattern: Using a mutable object (like a list or dictionary) as a default argument in a function definition.

Why it happens: Python evaluates default arguments once when the function is defined, not when it is called. That single object is shared across every subsequent execution.

AppSec Impact: In a web application (like FastAPI or Flask), if an endpoint uses a mutable default argument to store user sessions or request logs, User A's sensitive data can leak into User B's request.
"""
"Subsequent function call with no values will share what ever the default value has been updated to in previous calls."


"""
Flaw 2: Insecure Deserialization via pickle (Remote Code Execution)
The Antipattern: Using Python's built-in pickle module to load data received from untrusted sources (e.g., user cookies, API payloads, or uploaded files).

Why it happens: pickle doesn't just serialize data; it serializes Python object structures and execution bytecode.

AppSec Impact: Remote Code Execution (RCE). An attacker can craft a malicious pickled payload containing a __reduce__ method that executes arbitrary system commands (like rm -rf or reverse shells) the exact microsecond Python attempts to unpickle it.
"""

"""
Flaw 3: Command Injection via `subprocess` (`shell=True`)
The Antipattern: Spawning OS shell commands by passing a raw concatenated string into `subprocess` with `shell=True`.
Why it happens: Developers want quick execution of terminal commands and concatenate user input directly into the command string.
AppSec Impact: OS Command Injection. If user input is not sanitized, an attacker can append command separators (like `;`, `&&`, or `|`) to execute arbitrary terminal commands under your application's user permissions.
"""



"""
Flaw 4: Path Traversal (`..` Directory EscapesThe Antipattern: Naively concatenating user-supplied filenames directly into a base directory path.
Why it happens: Assuming `filename` will always be a simple file name rather than a relative path traversal sequence.
AppSec Impact: An attacker can supply `../../../../etc/passwd` to read sensitive server files, configuration keys, or source code.
"""

# from pathlib import Path

# base_dir = Path("/app/uploads/").resolve()
# user_input = "../../../etc/passwd"

# target_path = (base_dir / user_input).resolve()

# # Ensure the target path is strictly inside the base directory
# if not target_path.is_relative_to(base_dir):
#   raise PermissionError("Access denied: Path traversal detected.")


"""
Flaw 5: Timing Attacks on Secret Comparisons (`==`)
The Antipattern: Using standard equality operators (`==`) to verify API keys, password hashes, or cryptographic tokens.
Why it happens: Python's `==` operator compares strings/bytes character by character from left to right and short-circuits (returns `False` immediately) the moment it hits a mismatch.
AppSec Impact: Side-Channel Timing Attacks. An attacker can measure how many microseconds the server takes to reject a fake token. By analyzing response times down to the nanosecond, they can guess a secret key character by character.
""" # rate limiting

# import hmac

# # Safe: Takes the exact same amount of time regardless of where the mismatch is
# if hmac.compare_digest(user_token, actual_secret_token):
#   grant_access()


"""
Flaw 6: Unsafe YAML Loading (`yaml.load`)
The Antipattern: Using `yaml.load()` instead of `yaml.safe_load()` when parsing configuration files.
Why it happens: Older PyYAML documentation examples used `yaml.load()` by default.
AppSec Impact: Just like `pickle`, PyYAML's default loader can instantiate arbitrary Python classes and execute code during deserialization if fed a malicious YAML document.
"""


"""
Flaw 7: Insecure Type Juggling & Loose Validation in Custom Descriptors
The Antipattern: Writing weak type checks (like `type(val) == int` instead of `isinstance(val, int)`) that fail to account for subclass polymorphism.
Why it happens: Relying on exact type matching rather than structural protocols.
AppSec Impact: In Python, `bool` is a subclass of `int` (`isinstance(True, int)` evaluates to `True`). If a security control checks `isinstance(val, int)` to restrict an integer field (like user permissions or transfer amounts), passing a boolean value can bypass validation logic or cause unexpected type-juggling bugs.

The Secure Fix: Explicitly guard against booleans when integers are strictly required:
  ```python
  def validate_int(value):
    if isinstance(value, bool) or not isinstance(value, int):
      raise TypeError("Strict integer required (booleans not allowed).")
"""



'Do those 7 flaws cover every possible flaw in Python?'
'Verdict: Absolutely not. Those 7 are classic language-level and standard-library antipatterns. There are dozens of other categories, including ecosystem supply-chain vulnerabilities (malicious PyPI packages), SQL injection in ORMs, Server-Side Request Forgery (SSRF), insecure XML parsing (XXE via defusedxml), and "Zip Bombs" via the built-in zipfile module. Security is an ever-expanding landscape!"'

# __import__('os').system('rm -rf /')
# zipfile
# import ast libcst


####### Syllabus ##### Low-level Mechanics means understanding what the Python interpreter, the runtime memory, and the operating system are actually doing behind the curtain of your clean, high-level code.
# In short, high-level syntax is what you write; low-level mechanics are how the machine experiences what you wrote.
"""
How Long to Cover Python AppSec, Tools, and Resources
If you already have a solid foundation in Python, low-level mechanics, and object-oriented programming (which you do!), you can reach a professional, job-ready level in Python Application Security (AppSec) in about 3 to 6 months of consistent, hands-on study.

Here is a practical roadmap, along with the essential tools and resources:

Phase-by-Phase Timeline:
Weeks 1–4 (Secure Coding & Language Pitfalls): Mastering language-level vulnerabilities (like the ones we discussed: mutable defaults, insecure deserialization with pickle, type juggling, and timing attacks).

Weeks 5–8 (Web Application Security & OWASP Top 10 in Python): Securing web frameworks like FastAPI, Flask, or Django (handling SQL injection, XSS, CSRF, JWT validation errors, and broken access controls).

Weeks 9–12 (Tooling, SAST, & CI/CD Pipelines): Integrating automated security scanners into developer workflows and code repositories.

Months 4–6 (Advanced Defense & Supply Chain Security): Managing dependency vulnerabilities, writing custom AST scanners, and threat modeling.

Essential Tools to Master:
SAST (Static Application Security Testing):

Bandit: A tool designed specifically to find common security issues in Python source code.

Semgrep: A lightning-fast, highly customizable static analysis tool that lets you write custom security rules (like hunting for your own specific team antipatterns).

Ruff / Flake8-bandit: Linter plugins that catch security smells while you code.

Supply Chain & Dependency Scanners:

pip-audit / Safety: CLI tools that scan your requirements.txt or pyproject.toml against known vulnerabilities in PyPI packages (CVE databases).

Fuzz Testing:

Atheris: A coverage-guided Python fuzzer (by Google) used to find memory leaks, crashes, and unhandled exceptions in parsers and complex codebases.

Recommended Resources:
The OWASP Foundation: Specifically the OWASP Top 10, OWASP Python Security Project, and OWASP Cheat Sheet Series.

Books: Secure by Design (Manning) and The Tangled Web: A Guide to Securing Modern Web Applications (Michal Zalewski).

Hands-on Labs: PortSwigger Web Security Academy (free, industry gold standard for learning web app vulnerabilities and how to exploit/defend them).
"""



# Here is what the industry landscape looks like with the explosion of AI-generated code and agentic workflows:

# The Code Explosion: AI coding tools (like Cursor, GitHub Copilot, and coding agents) allow developers to ship 5x to 10x more code than before. However, AI models frequently replicate insecure coding patterns, hallucinate logic flaws, and introduce subtle vulnerabilities at scale.

# The Shift to AI Security & Pipeline Automation: Modern AppSec isn't just manually reviewing code anymore. Companies desperately need engineers who can build automated security tooling (like the AST scanners we just looked at), secure LLM integrations, handle prompt injections in agentic apps, and scale security checks inside fast-moving CI/CD pipelines.

# The Verdict: While basic, repetitive coding tasks are automated, security architecture, threat modeling, and deep code comprehension (especially in foundational languages like Python) remain high-value human skills. Organizations cannot automate strategic threat analysis or secure system design.

