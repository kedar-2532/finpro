export async function getTransactions(){
    const token = localStorage.getItem('access')

    const response = await fetch(
        'http://127.0.0.1:8000/api/finance/transactions/',
        {
            headers:{Authorization:`Bearer ${token}`}
        }
    )

if(!response.ok){
    throw new Error('Failed ot fetch')
}
return await response.json()

}

export async function deleteTransaction(id){
    const token=localStorage.getItem('access')

    const response=await fetch(
        `http://127.0.0.1:8000/api/finance/transactions/${id}/`,
        {
            method:'DELETE',

            headers:{
                Authorization:`Bearer ${token}`
            }
        }
    )
    if(!response.ok){
        throw new Error('Delete Failed')
    }
}

export async function addTransaction(data){
    const token = localStorage.getItem('access')
    const response = await fetch(
        "http://127.0.0.1:8000/api/finance/transactions/",
        {
            method:'POST',
            headers:{
                Authorization:`Bearer ${token}`,
                'Content-Type':'application/json'
            },
            body:JSON.stringify(data)
        }
    )
    if(!response.ok){
        throw new Error("Create Failed")
    }
    return await response.json()
}