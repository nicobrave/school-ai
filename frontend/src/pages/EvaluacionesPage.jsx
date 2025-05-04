import { useState, useEffect } from 'react'

export default function EvaluacionesPage() {
  const [items, setItems] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetch('/api/evaluaciones')
      .then(res => res.json())
      .then(data => {
        setItems(data)
        setLoading(false)
      })
      .catch(() => setLoading(false))
  }, [])

  if (loading) return <p>Cargando evaluaciones…</p>
  return (
    <div>
      <h1 className="text-2xl font-semibold mb-4">Evaluaciones Diferenciadas</h1>
      {items.length === 0
        ? <p className="text-text-secondary">No hay evaluaciones todavía.</p>
        : items.map(ev => (
          <div key={ev.id} className="card mb-4">
            <h2 className="text-xl font-bold">{ev.titulo}</h2>
            <p>{ev.descripcion}</p>
          </div>
        ))
      }
    </div>
  )
}
