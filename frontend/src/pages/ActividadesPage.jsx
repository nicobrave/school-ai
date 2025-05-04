import { useState, useEffect } from 'react'

export default function ActividadesPage() {
  const [acts, setActs] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetch('/api/actividades')
      .then(res => res.json())
      .then(data => {
        setActs(data)
        setLoading(false)
      })
      .catch(() => setLoading(false))
  }, [])

  if (loading) return <p>Cargando actividades…</p>
  return (
    <div>
      <h1 className="text-2xl font-semibold mb-4">Generador de Actividades</h1>
      {acts.length === 0
        ? <p className="text-text-secondary">Aún no hay actividades.</p>
        : acts.map(act => (
          <div key={act.id} className="card mb-4">
            <h2 className="text-xl font-bold">{act.titulo}</h2>
            <p>{act.instrucciones}</p>
          </div>
        ))
      }
    </div>
  )
}
