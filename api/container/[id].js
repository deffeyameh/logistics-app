import { createClient } from '@supabase/supabase-js'

const supabase = createClient(
  process.env.SUPABASE_URL,
  process.env.SUPABASE_KEY
)

export default async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*')

  const { id } = req.query

  const { data, error } = await supabase
    .from('containers')
    .select('*, products(*)')
    .eq('id', id)
    .single()

  if (error) return res.status(404).json({ error: 'ไม่พบข้อมูล' })

  res.json(data)
}
