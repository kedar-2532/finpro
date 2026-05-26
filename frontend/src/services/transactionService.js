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
        `http://127.0.0.1:8000/api/finance/transactions/${id}`,
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