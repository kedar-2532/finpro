import { useState } from 'react'

function AddTransactionform({ onAdd }){

    const [form, setForm]=useState({
        account:1,
        category:1,
        amount:"",
        transaction_type:"INCOME",
        description:"",
        date:""
    })
function handleChange(e){
    setForm({
        ...form,
        [e.target.name]:e.target.value 
    })
}
async function handleSubmit(e){
    e.preventDefault()
    await onAdd(form)
    setForm({
        account:1,
        category:1,
        amount:"",
        transaction_type:"INCOME",
        description:"",
        date:""
    })
}
return(
    <div className='bg-white p-5 rounded-xl shadow mb-6'>

        <h2 className='text-xl font-bold mn-4'>Add Transaction</h2>

        <form onSubmit={handleSubmit} className='grid grid-cols-2 pag-3'>

            <input name="amount" placeholder='Amount' value={form.amount} onChange={handleChange} className='border p-2' />

            <input name="description" placeholder='Description' value={form.description} onChange={handleChange} className='border p-2' />

            <select name="transaction_type" value={form.transaction_type} onChange={handleChange} className='border p-2'>
                <option>INCOME</option>
                <option>EXPENSE</option>
            </select>

            <input type='datetime-local' name="date" value={form.date} onChange={handleChange} className='border p-2' />

            <button className='bg-blue-600 text-white p-2 rounded'>Add</button>

        </form>
    </div>
)
}

export default AddTransactionform

