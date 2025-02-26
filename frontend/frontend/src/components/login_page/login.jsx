import React, { useState } from "react";
import "../login_page/login.css";
import axios from "axios";

function Login() {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(""); // ✅ Added missing state for error

    async function isValid(e) {
        e.preventDefault();

        if (!email || !password) {
            setError("Both fields are needed");
            setLoading(false);
            return;
        }

        try {
            setLoading(true);
            const response = await axios.post("some.url", {
                email,
                password,
            });
            alert("Login Successful");
            console.log(response.data);
        } catch (err) { 
            setError(err.response?.data?.message || "Login failed");
        } finally {
            setLoading(false); 
        }
    }

    return (
        <div className="login-container">
            <h1>
                Login 
            </h1>
            {error && <p className="error-message">{error}</p>}
            <form onSubmit={isValid}>
                <input
                    placeholder="Email"
                    type="email"
                    onChange={(e) => setEmail(e.target.value)}
                    value={email}
                />
                
                <input
                    placeholder="Password"
                    type="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />
                
                <button type="submit" disabled={loading}>
                    {loading ? "Logging in..." : "Login"}
                </button>
            </form>
        </div>
    );
}

export default Login;
