import React from 'react'
import CIcon from '@coreui/icons-react'

const _nav =  [
  {
    _tag: 'CSidebarNavItem',
    name: 'Dashboard',
    to: '/dashboard',
    icon: <CIcon name="cil-speedometer" customClasses="c-sidebar-nav-icon"/>,
  },
  {
    _tag: 'CSidebarNavTitle',
    _children: ['Scan']
  },
  {
    _tag: 'CSidebarNavDropdown',
    name: 'Scanner',
    route: '/scan',
    icon: 'cil-puzzle',
    _children: [
      {
        _tag: 'CSidebarNavItem',
        name: 'Web scan',
        to: '/scan/webscan',
      },
      {
        _tag: 'CSidebarNavItem',
        name: 'Network scan',
        to: '/scan/netscan',
      },
    ],
  },

]

export default _nav
