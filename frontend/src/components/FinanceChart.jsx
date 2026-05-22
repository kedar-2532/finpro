import{ PieChart, Pie, Cell, Tooltip, Legend } from 'recharts';

function FinanceChart({ income, expense }) {

    const data = [{name:"Income", value:income},{name:'Expense', value:expense}]

    const COLORS=['#22C55E', '#EF4444']

    return (
        <div className='bg-white p-5 rounded-xl shadow'>

            <h2 className='text-xl font-bold mb-4'>
                Income vs Expense
            </h2>

            <PieChart width={300} height={250}>

                <Pie data={data} dataKey='value' outerRadius={80}>
                    
                    {
                        data.map(
                            (_,index)=>(
                                <Cell key={index} fill={COLORS[index]}/>
                            )
                        )
                    }

                </Pie>

                <Tooltip/>

                <Legend/>

            </PieChart>
        
        </div>
    )
}

export default FinanceChart
