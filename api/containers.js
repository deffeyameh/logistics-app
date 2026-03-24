import { createClient } from '@supabase/supabase-js'

const supabase = createClient(
  process.env.SUPABASE_URL,
  process.env.SUPABASE_KEY
)

export default async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*')
  
  const { 
    page = 1, 
    limit = 50, 
    search = '', 
    transport = 'all',
    branch_ids = ''
  } = req.query

  const from = (page - 1) * limit
  const to = from + parseInt(limit) - 1

  let query = supabase
    .from('containers')
    .select('*, products(*)', { count: 'exact' })
    .order('id', { ascending: false })
    .range(from, to)

  if (search) {
    query = query.ilike('sm_code', `%${search}%`)
  }

  if (transport !== 'all') {
    query = query.ilike('transport_name', transport)
  }

  if (branch_ids) {
    const ids = branch_ids.split(',').map(Number)
    query = query.in('branch_id', ids)
  }

  const { data, error, count } = await query

  if (error) return res.status(500).json({ error: error.message })

  res.json({
    data,
    total: count,
    page: parseInt(page),
    last_page: Math.ceil(count / limit)
  })
}
