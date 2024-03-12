import { useLocation, Navigate } from "react-router-dom";

export const setToken = (token: string): void => {
    localStorage.setItem('access_token', token);
};

export const fetchToken = (): string | null => {
    return localStorage.getItem('access_token');
};

const RequireToken: React.FC<{ children: React.ReactNode }> = ({ children }) => {
    const auth = fetchToken();
    const location = useLocation();

    return (
        auth ? <>{children}</> : <Navigate to='/' state={{ from: location }} />
    );
};

export default RequireToken;
