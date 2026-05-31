import { PieChart, Pie, Cell, Tooltip, Legend, ResponsiveContainer } from 'recharts'


function CategoryPieChart({ data }) {
  
    const expenseData = data.filter(item=> item.type === "EXPENSE");
    if (expenseData.length === 0){
        return(
            <div className='bg-white p-5 rounded-xl shadow mt-6'>
                
                <h2 className='text-xl font-bold mb-4'>Expense By Category</h2>

                <p className='text-gray-500'>No Expense data available yet.</p>

            </div>
        );
    }
    return (
        <div className='bg-white p-5 rounded-xl shadow mt-6'>

            <h2 className='text-xl font-bold mb-4'>Expense By Category</h2>
            
            <div className='w-full h-[350px]'>

                <pre>{JSON.stringify(expenseData, null, 2)}</pre>

                <ResponsiveContainer width='100%' height='100%'>

                    <PieChart>
                        
                        <Pie data={expenseData} dataKey='total' nameKey='category' cx='50%' cy='50%' outerRadius={120} fill='#8884d8' label>

                            {
                                expenseData.map(
                                    (_, index)=>( 
                                    <Cell key={index} />
                                )
                            )
                            }

                        </Pie>
                        
                        <Tooltip />
                        
                        <Legend />
                    
                    </PieChart>

                </ResponsiveContainer>

            </div>

        </div>
  )
}

export default CategoryPieChart;
