# Centralized Secret Management System using AWS Secrets Manager and IAM Policies  

# 📌 Project Overview

This project demonstrates how to securely manage sensitive information like database credentials using AWS Secrets Manager instead of hardcoding them in the application code.  
The application runs on an EC2 instance and retrieves secrets dynamically using IAM role-based access, improving security and eliminating hardcoded credentials.


---

# 🏗️ Architecture

![Architecture diagram](https://github.com/Sakshigond12/aws-secrets-manager-project/blob/955c5c2122cade7d53f65840d6d2eca4341225f2/image/Architechture%20diagram.png)

---

# ⚙️ Technologies Used

- AWS EC2  
- AWS Secrets Manager  
- AWS IAM  
- Python (boto3)  

---

# 📂 Project Structure

```bash
aws-secrets-manager-project
│
├── app-secret.py                 
├── iam policy.json         
├── README.md             
└── image/
    └── ec2-instance.png 
    └── secret-output.png
```
---

# 💻Commands to Run the Project

### 1️⃣Connect to your EC2 instance

```bash
ssh -i your-key.pem ec2-user@<EC2_PUBLIC_IP>

```
---
### 2️⃣Update the system

```bash
sudo yum update -y       # Amazon Linux
sudo apt update -y       # Ubuntu
```
---
### 3️⃣Install Python3 and pip 

```bash
sudo yum install python3 -y       # Amazon Linux
sudo apt install python3-pip -y   # Ubuntu
```
---
### 4️⃣ Create a virtual environment
```bash
python3 -m venv myenv
```
---

### 5️⃣Activate the virtual environment
```bash
source myenv/bin/activate
```
---



### 6️⃣Install boto3
```bash
pip3 install boto3
```
----

### 7️⃣Run the application
```bash
python3 app-sercret.py
```

---
# 📸 Project Output 

### 1 Ec2-instance
![ec2-instance](https://github.com/Sakshigond12/aws-secrets-manager-project/blob/955c5c2122cade7d53f65840d6d2eca4341225f2/image/ec2-instance.png)

---

### 2 Secret Retrieval Output
![Secret Retrieval Output](https://github.com/Sakshigond12/aws-secrets-manager-project/blob/955c5c2122cade7d53f65840d6d2eca4341225f2/image/secret%20retriavel%20output.png)

---

# 🔄 Why Secret Rotation Matters

- Reduces risk of credential leakage 

- Limits exposure if credentials are compromised

- Improves overall system security
- Helps follow security best practices

- AWS Secrets Manager supports automatic secret rotation, which can be enabled for further security.

---

# 🔐 Security Improvements

- Removed hardcoded credentials

- Stored secrets securely in AWS Secrets Manager

- Used IAM roles instead of access keys

- Controlled access using IAM policies (least privilege)

- Prevented unauthorized access

- Optional: enabled automatic secret rotation

---

# 🎉Conclusion

This project demonstrates a secure secret management system using AWS Secrets Manager and IAM roles.  
It eliminates hardcoded credentials, allows dynamic secret retrieval, improves security, and follows best practices for cloud applications.



---

# 👩‍💻Author

**Sakshi Gond**

Aspiring Cloud & DevOps Engineer  

🔗 GitHub: https://github.com/Sakshigond12  
🔗 LinkedIn: https://linkedin.com/in/sakshi-gond-9ab9092a2
