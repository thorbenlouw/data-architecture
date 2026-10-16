# Security and access

* [Security and access](security.md) - Protect data from unauthorised access, loss and misuse.
  * [Access control](access-control.md) - Decide who can see and change which data, at every level from account down to individual values.
    * [Access requests and reviews](access-requests.md) - Let people request access to data, have owners approve and time-limit it, and review existing access on a regular cycle.
    * [Attribute- and tag-based access control](attribute-based-access.md) - Grant or deny access based on attributes of the user and tags on the data.
    * [Column security and dynamic masking](column-masking.md) - Hide or mask sensitive columns depending on who is querying.
    * [Privileged access management](privileged-access.md) - Grant administrator, emergency and vendor support access to the platform only when needed, with approval, time limits and a record of what was done.
    * [Role-based access control](role-based-access.md) - Grant permissions to roles and assign roles to people and groups.
    * [Row-level security](row-level-security.md) - Restrict which rows each user sees based on who they are.
  * [AI supply chain security](ai-supply-chain-security.md) - Check third-party models, model files, libraries and tool servers for tampering and malicious code before use, and record what each AI system is built from.
  * [Audit logging](audit-logging.md) - Record who accessed or changed what, when and from where, and keep the records tamper-evident.
  * [Data breach response](data-breach-response.md) - Work out which data and which people a security incident exposed, assess the risk, and notify regulators and affected individuals within legal deadlines, keeping a record of each decision.
  * [Data loss prevention](data-loss-prevention.md) - Detect and block sensitive data leaving approved boundaries.
  * [Data security posture management](data-security-posture.md) - Find continuously where sensitive data lives, who can reach it and which configurations put it at risk.
  * [Data threat detection](data-threat-detection.md) - Analyse data access behaviour to detect and respond to insider threats, ransomware and abnormal access.
  * [Encryption](encryption.md) - Encrypt data at rest and in transit, with keys managed securely.
    * [Crypto-shredding](crypto-shredding.md) - Make specific data unreadable everywhere, including in backups, by destroying the encryption keys that protect it.
    * [Cryptographic agility](cryptographic-agility.md) - Inventory the cryptography protecting data and change algorithms, for example to post-quantum ciphers, without rework.
    * [Customer-managed keys](customer-managed-keys.md) - Encrypt platform data with keys you control, so you can rotate or revoke them.
  * [Identity and authentication](identity-authentication.md) - Authenticate people and services through central identity, single sign-on and short-lived credentials.
    * [External user and tenant identity](external-identity.md) - Manage identities, tenants and permissions for customers and partners who use data products or embedded analytics.
  * [Network security](network-security.md) - Keep data traffic on private networks and restrict where the platform can be reached from.
  * [Secrets management](secrets-management.md) - Store and rotate the credentials and keys used by pipelines and tools without putting them in code.
  * [Shared compute isolation](compute-user-isolation.md) - Sandbox each user's code on shared compute so nobody can bypass access controls or affect other users.

# Also part of this domain

* [Agent identity and authorisation](../generative-ai/agent-identity.md) (main home: Generative AI) - Give each agent its own identity and scoped, short-lived access to data on behalf of named users, enforced at request time.
* [De-identification](../governance/deidentification.md) (main home: Governance and compliance) - Pseudonymise, tokenise or anonymise data so it can be used with less privacy risk.
* [Permission-aware retrieval](../generative-ai/permission-aware-retrieval.md) (main home: Generative AI) - Filter retrieved content by each user's permissions in the source systems so AI answers never reveal what the user could not open.
* [Storage credential vending](../storage/credential-vending.md) (main home: Storage and table management) - Have the catalogue issue short-lived, table-scoped storage credentials to engines so they never hold broad storage access.
