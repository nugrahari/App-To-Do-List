export const getBgColor = (val) => {
    if (val == 'TO DO') {
        return 'bg-blue-300'
    } else if (val == 'IN PROGRESS') {
        return 'bg-orange-300'
    } else if (val == 'SCRIPT TESTING') {
        return 'bg-pink-800'
    } else if (val == 'DONE') {
        return 'bg-green-300'
    } else {
        return 'bg-slate-300'
    }
}

export const getColorPriority = (val) => {
    if (val == 'High') {
        return 'danger'
    } else if (val == 'Medium') {
        return 'warning'
    } else if (val == 'LOW') {
        return 'info'
    } else {
        return 'primary'
    }
}

export const getSingkatanPriority = (val) => {
    if (val == 'High') {
        return 'h'
    } else if (val == 'Medium') {
        return 'm'
    } else if (val == 'Low') {
        return 'L'
    } 
}


export const getColor = (val) => {
    if (val == 'TO DO') {
        return 'text-blue-300'
    } else if (val == 'IN PROGRESS') {
        return 'text-orange-300'
    } else if (val == 'SCRIPT TESTING') {
        return 'text-pink-800'
    } else if (val == 'DONE') {
        return 'text-green-300'
    } else {
        return 'text-slate-300'
    }
}



