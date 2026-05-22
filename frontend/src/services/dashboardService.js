export async function getDashboardData() {
    
    const token = localStorage.getItem('access')

    const response = await fetch(
        "http://127.0.0.1:8000/api/finance/dashboard/",
        {
            headers:{
                Authorization:`Bearer ${token}`
            }
        }
    )
    return response.json()
}