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
    route: '/scans',
    icon: 'cil-puzzle',
    _children: [
      {
        _tag: 'CSidebarNavItem',
        name: 'Web scan',
        to: '/scans/webscan',
      },
      {
        _tag: 'CSidebarNavItem',
        name: 'Network scan',
        to: '/scans/netscan',
      },
    ],
  },
  {
    _tag: 'CSidebarNavItem',
    name: 'Result',
    icon: 'cil-puzzle',
    to: '/result',
  },

]

export default _nav
