import { Outlet } from 'react-router-dom'
import HeaderDocente from './HeaderDocente'

export default function Layout() {
  return (
    <div className="min-h-screen bg-background text-text-primary">
      <HeaderDocente />
      <main className="max-w-6xl mx-auto p-6">
        <Outlet />
      </main>
    </div>
  )
}
