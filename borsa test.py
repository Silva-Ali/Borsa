<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Profesyonel BIST hisse senedi trading simülatörü">
    <title>BIST Trader Pro - Professional Edition</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/3.9.1/chart.min.js"></script>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        :root {
            --color-primary: #0ea5e9;
            --color-primary-hover: #0284c7;
            --color-success: #22c55e;
            --color-success-hover: #16a34a;
            --color-danger: #ef4444;
            --color-danger-hover: #dc2626;
            --color-warning: #f59e0b;
            --color-info: #3b82f6;
            
            --bg-primary: #0f172a;
            --bg-secondary: #1e293b;
            --bg-tertiary: #334155;
            --bg-hover: #475569;
            
            --text-primary: #f8fafc;
            --text-secondary: #cbd5e1;
            --text-muted: #94a3b8;
            
            --border-color: #334155;
            --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.3);
            --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.3);
            --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.4);
            --shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.5);
            
            --radius-sm: 0.375rem;
            --radius-md: 0.5rem;
            --radius-lg: 0.75rem;
            --radius-xl: 1rem;
            
            --transition-fast: 150ms cubic-bezier(0.4, 0, 0.2, 1);
            --transition-base: 200ms cubic-bezier(0.4, 0, 0.2, 1);
            --transition-slow: 300ms cubic-bezier(0.4, 0, 0.2, 1);
        }
        
        [data-theme="light"] {
            --bg-primary: #f8fafc;
            --bg-secondary: #ffffff;
            --bg-tertiary: #f1f5f9;
            --bg-hover: #e2e8f0;
            
            --text-primary: #0f172a;
            --text-secondary: #475569;
            --text-muted: #64748b;
            
            --border-color: #e2e8f0;
            --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
            --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
            --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.15);
            --shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.2);
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Helvetica Neue', sans-serif;
            background: var(--bg-primary);
            color: var(--text-primary);
            line-height: 1.5;
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
            transition: background-color var(--transition-base), color var(--transition-base);
        }
        
        .container {
            max-width: 1600px;
            margin: 0 auto;
            padding: 1rem;
        }
        
        @media (min-width: 640px) {
            .container {
                padding: 1.5rem;
            }
        }
        
        /* Typography */
        .text-xs { font-size: 0.75rem; line-height: 1rem; }
        .text-sm { font-size: 0.875rem; line-height: 1.25rem; }
        .text-base { font-size: 1rem; line-height: 1.5rem; }
        .text-lg { font-size: 1.125rem; line-height: 1.75rem; }
        .text-xl { font-size: 1.25rem; line-height: 1.75rem; }
        .text-2xl { font-size: 1.5rem; line-height: 2rem; }
        .text-3xl { font-size: 1.875rem; line-height: 2.25rem; }
        
        .font-medium { font-weight: 500; }
        .font-semibold { font-weight: 600; }
        .font-bold { font-weight: 700; }
        
        /* Header */
        .header {
            background: var(--bg-secondary);
            border-radius: var(--radius-xl);
            padding: 1.25rem;
            margin-bottom: 1.5rem;
            box-shadow: var(--shadow-md);
        }
        
        .header-top {
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 1rem;
            margin-bottom: 1.25rem;
            flex-wrap: wrap;
        }
        
        .logo {
            display: flex;
            align-items: center;
            gap: 0.75rem;
            font-size: 1.5rem;
            font-weight: 700;
            color: var(--color-primary);
            user-select: none;
        }
        
        .logo-icon {
            font-size: 1.75rem;
        }
        
        .header-actions {
            display: flex;
            gap: 0.5rem;
            flex-wrap: wrap;
        }
        
        /* Buttons */
        .btn {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 0.5rem;
            padding: 0.625rem 1rem;
            font-size: 0.875rem;
            font-weight: 600;
            border: none;
            border-radius: var(--radius-md);
            cursor: pointer;
            transition: all var(--transition-fast);
            white-space: nowrap;
            user-select: none;
        }
        
        .btn:disabled {
            opacity: 0.5;
            cursor: not-allowed;
        }
        
        .btn:active:not(:disabled) {
            transform: scale(0.98);
        }
        
        .btn-primary {
            background: var(--color-primary);
            color: white;
        }
        
        .btn-primary:hover:not(:disabled) {
            background: var(--color-primary-hover);
            box-shadow: var(--shadow-md);
        }
        
        .btn-success {
            background: var(--color-success);
            color: white;
        }
        
        .btn-success:hover:not(:disabled) {
            background: var(--color-success-hover);
            box-shadow: var(--shadow-md);
        }
        
        .btn-danger {
            background: var(--color-danger);
            color: white;
        }
        
        .btn-danger:hover:not(:disabled) {
            background: var(--color-danger-hover);
            box-shadow: var(--shadow-md);
        }
        
        .btn-secondary {
            background: var(--bg-tertiary);
            color: var(--text-primary);
        }
        
        .btn-secondary:hover:not(:disabled) {
            background: var(--bg-hover);
        }
        
        .btn-ghost {
            background: transparent;
            color: var(--text-secondary);
        }
        
        .btn-ghost:hover:not(:disabled) {
            background: var(--bg-tertiary);
            color: var(--text-primary);
        }
        
        .btn-sm {
            padding: 0.375rem 0.75rem;
            font-size: 0.8125rem;
        }
        
        .btn-lg {
            padding: 0.75rem 1.5rem;
            font-size: 1rem;
        }
        
        /* Stats Grid */
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
            margin-bottom: 1.5rem;
        }
        
        .stat-card {
            background: var(--bg-secondary);
            border-radius: var(--radius-lg);
            padding: 1.25rem;
            box-shadow: var(--shadow-sm);
            transition: all var(--transition-base);
        }
        
        .stat-card:hover {
            box-shadow: var(--shadow-md);
            transform: translateY(-2px);
        }
        
        .stat-label {
            font-size: 0.875rem;
            color: var(--text-muted);
            margin-bottom: 0.5rem;
            font-weight: 500;
        }
        
        .stat-value {
            font-size: 1.75rem;
            font-weight: 700;
            color: var(--text-primary);
            margin-bottom: 0.25rem;
        }
        
        .stat-change {
            font-size: 0.875rem;
            font-weight: 600;
        }
        
        .text-success { color: var(--color-success); }
        .text-danger { color: var(--color-danger); }
        .text-warning { color: var(--color-warning); }
        .text-muted { color: var(--text-muted); }
        
        /* Tabs */
        .tabs {
            display: flex;
            gap: 0.5rem;
            margin-bottom: 1.5rem;
            overflow-x: auto;
            scrollbar-width: none;
            -ms-overflow-style: none;
        }
        
        .tabs::-webkit-scrollbar {
            display: none;
        }
        
        .tab {
            padding: 0.75rem 1.25rem;
            background: var(--bg-secondary);
            border: 2px solid transparent;
            border-radius: var(--radius-md);
            color: var(--text-secondary);
            font-weight: 600;
            font-size: 0.875rem;
            cursor: pointer;
            white-space: nowrap;
            transition: all var(--transition-fast);
            user-select: none;
        }
        
        .tab:hover {
            background: var(--bg-tertiary);
            color: var(--text-primary);
        }
        
        .tab.active {
            background: var(--color-primary);
            color: white;
            box-shadow: var(--shadow-md);
        }
        
        .tab-content {
            display: none;
        }
        
        .tab-content.active {
            display: block;
            animation: fadeIn var(--transition-slow);
        }
        
        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(8px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        /* Layout */
        .main-grid {
            display: grid;
            grid-template-columns: 1fr;
            gap: 1.5rem;
        }
        
        @media (min-width: 1024px) {
            .main-grid {
                grid-template-columns: 1fr 400px;
            }
        }
        
        .panel {
            background: var(--bg-secondary);
            border-radius: var(--radius-lg);
            padding: 1.5rem;
            box-shadow: var(--shadow-sm);
        }
        
        .panel-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1.25rem;
            gap: 1rem;
        }
        
        .panel-title {
            font-size: 1.25rem;
            font-weight: 700;
            color: var(--text-primary);
        }
        
        /* Search */
        .search-container {
            position: relative;
            margin-bottom: 1rem;
        }
        
        .search-icon {
            position: absolute;
            left: 1rem;
            top: 50%;
            transform: translateY(-50%);
            color: var(--text-muted);
            pointer-events: none;
        }
        
        .search-input {
            width: 100%;
            padding: 0.75rem 1rem 0.75rem 2.75rem;
            background: var(--bg-primary);
            border: 2px solid var(--border-color);
            border-radius: var(--radius-md);
            color: var(--text-primary);
            font-size: 0.875rem;
            transition: all var(--transition-fast);
        }
        
        .search-input:focus {
            outline: none;
            border-color: var(--color-primary);
            box-shadow: 0 0 0 3px rgba(14, 165, 233, 0.1);
        }
        
        .search-input::placeholder {
            color: var(--text-muted);
        }
        
        /* Stock List */
        .stock-list {
            max-height: 650px;
            overflow-y: auto;
            padding-right: 0.5rem;
        }
        
        .stock-list::-webkit-scrollbar {
            width: 6px;
        }
        
        .stock-list::-webkit-scrollbar-track {
            background: transparent;
        }
        
        .stock-list::-webkit-scrollbar-thumb {
            background: var(--border-color);
            border-radius: 3px;
        }
        
        .stock-list::-webkit-scrollbar-thumb:hover {
            background: var(--bg-hover);
        }
        
        .stock-item {
            position: relative;
            background: var(--bg-primary);
            border: 2px solid var(--border-color);
            border-radius: var(--radius-lg);
            padding: 1rem;
            margin-bottom: 0.75rem;
            cursor: pointer;
            transition: all var(--transition-fast);
        }
        
        .stock-item:hover {
            border-color: var(--color-primary);
            transform: translateX(4px);
            box-shadow: var(--shadow-md);
        }
        
        .stock-item:active {
            transform: translateX(2px);
        }
        
        .stock-header {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 0.5rem;
        }
        
        .stock-info {
            flex: 1;
            min-width: 0;
        }
        
        .stock-symbol {
            font-weight: 700;
            font-size: 1.125rem;
            color: var(--text-primary);
            margin-bottom: 0.25rem;
        }
        
        .stock-name {
            font-size: 0.875rem;
            color: var(--text-muted);
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }
        
        .stock-price-info {
            text-align: right;
            flex-shrink: 0;
        }
        
        .stock-price {
            font-weight: 700;
            font-size: 1.125rem;
            color: var(--text-primary);
            margin-bottom: 0.25rem;
        }
        
        .stock-change {
            font-size: 0.875rem;
            font-weight: 600;
            display: flex;
            align-items: center;
            gap: 0.25rem;
            justify-content: flex-end;
        }
        
        .stock-meta {
            display: flex;
            gap: 1rem;
            font-size: 0.75rem;
            color: var(--text-muted);
            margin-top: 0.5rem;
        }
        
        .stock-meta-item {
            display: flex;
            align-items: center;
            gap: 0.25rem;
        }
        
        .watchlist-btn {
            position: absolute;
            top: 0.75rem;
            right: 0.75rem;
            background: none;
            border: none;
            font-size: 1.25rem;
            cursor: pointer;
            opacity: 0.3;
            transition: all var(--transition-fast);
            padding: 0.25rem;
            line-height: 1;
        }
        
        .watchlist-btn:hover {
            opacity: 1;
            transform: scale(1.2);
        }
        
        .watchlist-btn.active {
            opacity: 1;
        }
        
        /* Modal */
        .modal {
            display: none;
            position: fixed;
            inset: 0;
            background: rgba(0, 0, 0, 0.75);
            backdrop-filter: blur(4px);
            z-index: 1000;
            padding: 1rem;
            overflow-y: auto;
        }
        
        .modal.active {
            display: flex;
            justify-content: center;
            align-items: flex-start;
            padding-top: 2rem;
            animation: modalFadeIn var(--transition-base);
        }
        
        @keyframes modalFadeIn {
            from {
                opacity: 0;
            }
            to {
                opacity: 1;
            }
        }
        
        .modal-content {
            background: var(--bg-secondary);
            border-radius: var(--radius-xl);
            padding: 2rem;
            max-width: 900px;
            width: 100%;
            max-height: 90vh;
            overflow-y: auto;
            box-shadow: var(--shadow-xl);
            animation: modalSlideUp var(--transition-slow);
        }
        
        @keyframes modalSlideUp {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        .modal-content::-webkit-scrollbar {
            width: 6px;
        }
        
        .modal-content::-webkit-scrollbar-track {
            background: transparent;
        }
        
        .modal-content::-webkit-scrollbar-thumb {
            background: var(--border-color);
            border-radius: 3px;
        }
        
        .modal-header {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 1.5rem;
            gap: 1rem;
        }
        
        .modal-title {
            font-size: 1.5rem;
            font-weight: 700;
            color: var(--text-primary);
        }
        
        .modal-subtitle {
            color: var(--text-muted);
            font-size: 0.875rem;
            margin-top: 0.25rem;
        }
        
        /* Detail Grid */
        .detail-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
            gap: 1rem;
            margin-bottom: 1.5rem;
        }
        
        .detail-card {
            background: var(--bg-primary);
            padding: 1rem;
            border-radius: var(--radius-md);
            text-align: center;
            transition: all var(--transition-fast);
        }
        
        .detail-card:hover {
            background: var(--bg-tertiary);
        }
        
        .detail-label {
            font-size: 0.75rem;
            color: var(--text-muted);
            margin-bottom: 0.5rem;
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        
        .detail-value {
            font-size: 1.25rem;
            font-weight: 700;
            color: var(--text-primary);
        }
        
        /* Indicators */
        .indicators-section {
            background: var(--bg-primary);
            border-radius: var(--radius-md);
            padding: 1.25rem;
            margin-bottom: 1.5rem;
        }
        
        .indicators-title {
            font-weight: 600;
            margin-bottom: 1rem;
            color: var(--text-primary);
        }
        
        .indicators-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
            gap: 1rem;
        }
        
        .indicator-item {
            text-align: center;
        }
        
        .indicator-label {
            font-size: 0.75rem;
            color: var(--text-muted);
            margin-bottom: 0.5rem;
            font-weight: 500;
        }
        
        .indicator-value {
            font-weight: 700;
            font-size: 1.125rem;
            color: var(--text-primary);
            margin-bottom: 0.5rem;
        }
        
        .indicator-signal {
            display: inline-block;
            padding: 0.25rem 0.75rem;
            border-radius: var(--radius-sm);
            font-size: 0.75rem;
            font-weight: 600;
        }
        
        .signal-buy {
            background: rgba(34, 197, 94, 0.2);
            color: var(--color-success);
        }
        
        .signal-sell {
            background: rgba(239, 68, 68, 0.2);
            color: var(--color-danger);
        }
        
        .signal-neutral {
            background: var(--bg-tertiary);
            color: var(--text-muted);
        }
        
        /* Trade Section */
        .trade-tabs {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 0.75rem;
            margin-bottom: 1.5rem;
        }
        
        .trade-tab {
            padding: 0.875rem;
            border: 2px solid var(--border-color);
            border-radius: var(--radius-md);
            background: var(--bg-primary);
            color: var(--text-primary);
            font-weight: 600;
            cursor: pointer;
            text-align: center;
            transition: all var(--transition-fast);
            user-select: none;
        }
        
        .trade-tab:hover {
            background: var(--bg-tertiary);
        }
        
        .trade-tab.active-buy {
            background: var(--color-success);
            border-color: var(--color-success);
            color: white;
            box-shadow: var(--shadow-md);
        }
        
        .trade-tab.active-sell {
            background: var(--color-danger);
            border-color: var(--color-danger);
            color: white;
            box-shadow: var(--shadow-md);
        }
        
        .input-group {
            margin-bottom: 1rem;
        }
        
        .input-label {
            display: block;
            font-size: 0.875rem;
            font-weight: 600;
            margin-bottom: 0.5rem;
            color: var(--text-primary);
        }
        
        .input-field {
            width: 100%;
            padding: 0.75rem;
            background: var(--bg-primary);
            border: 2px solid var(--border-color);
            border-radius: var(--radius-md);
            color: var(--text-primary);
            font-size: 1rem;
            font-weight: 600;
            text-align: center;
            transition: all var(--transition-fast);
        }
        
        .input-field:focus {
            outline: none;
            border-color: var(--color-primary);
            box-shadow: 0 0 0 3px rgba(14, 165, 233, 0.1);
        }
        
        .input-field::placeholder {
            color: var(--text-muted);
        }
        
        .quick-buttons {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 0.5rem;
            margin-bottom: 1rem;
        }
        
        .quick-btn {
            padding: 0.625rem;
            background: var(--bg-primary);
            border: 2px solid var(--border-color);
            border-radius: var(--radius-md);
            color: var(--text-primary);
            font-weight: 600;
            font-size: 0.875rem;
            cursor: pointer;
            transition: all var(--transition-fast);
            user-select: none;
        }
        
        .quick-btn:hover {
            background: var(--color-primary);
            border-color: var(--color-primary);
            color: white;
            transform: translateY(-2px);
            box-shadow: var(--shadow-md);
        }
        
        .quick-btn:active {
            transform: translateY(0);
        }
        
        .summary-box {
            background: var(--bg-primary);
            border-radius: var(--radius-md);
            padding: 1rem;
            margin-bottom: 1rem;
        }
        
        .summary-row {
            display: flex;
            justify-content: space-between;
            margin-bottom: 0.75rem;
            font-size: 0.875rem;
        }
        
        .summary-row:last-child {
            margin-bottom: 0;
            padding-top: 0.75rem;
            border-top: 1px solid var(--border-color);
            font-weight: 600;
        }
        
        /* Chart */
        .chart-container {
            margin: 1rem 0;
            padding: 1rem;
            background: var(--bg-primary);
            border-radius: var(--radius-md);
        }
        
        /* Empty State */
        .empty-state {
            text-align: center;
            padding: 4rem 2rem;
            color: var(--text-muted);
        }
        
        .empty-icon {
            font-size: 3rem;
            margin-bottom: 1rem;
            opacity: 0.5;
        }
        
        .empty-text {
            font-size: 1rem;
        }
        
        /* Notification */
        .notification {
            position: fixed;
            top: 1rem;
            right: 1rem;
            background: var(--bg-secondary);
            padding: 1rem 1.5rem;
            border-radius: var(--radius-md);
            box-shadow: var(--shadow-xl);
            z-index: 2000;
            animation: slideInRight var(--transition-slow);
            max-width: 400px;
            border-left: 4px solid var(--color-primary);
            display: flex;
            align-items: center;
            gap: 0.75rem;
        }
        
        @keyframes slideInRight {
            from {
                transform: translateX(400px);
                opacity: 0;
            }
            to {
                transform: translateX(0);
                opacity: 1;
            }
        }
        
        .notification.success {
            border-left-color: var(--color-success);
        }
        
        .notification.error {
            border-left-color: var(--color-danger);
        }
        
        .notification.warning {
            border-left-color: var(--color-warning);
        }
        
        .notification-icon {
            font-size: 1.25rem;
            flex-shrink: 0;
        }
        
        .notification-text {
            font-size: 0.875rem;
            font-weight: 500;
        }
        
        /* History */
        .history-item {
            background: var(--bg-primary);
            border-radius: var(--radius-md);
            padding: 1rem;
            margin-bottom: 0.75rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            transition: all var(--transition-fast);
        }
        
        .history-item:hover {
            background: var(--bg-tertiary);
        }
        
        .history-badge {
            display: inline-block;
            padding: 0.25rem 0.75rem;
            border-radius: var(--radius-sm);
            font-size: 0.75rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
        }
        
        .badge-buy {
            background: rgba(34, 197, 94, 0.2);
            color: var(--color-success);
        }
        
        .badge-sell {
            background: rgba(239, 68, 68, 0.2);
            color: var(--color-danger);
        }
        
        /* Settings */
        .settings-section {
            margin-bottom: 2rem;
        }
        
        .settings-section:last-child {
            margin-bottom: 0;
        }
        
        .settings-section-title {
            font-weight: 600;
            margin-bottom: 1rem;
            color: var(--text-primary);
        }
        
        .settings-item {
            background: var(--bg-primary);
            border-radius: var(--radius-md);
            padding: 1rem;
            margin-bottom: 0.75rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 1rem;
        }
        
        .settings-info h4 {
            font-weight: 600;
            margin-bottom: 0.25rem;
            color: var(--text-primary);
        }
        
        .settings-info p {
            font-size: 0.875rem;
            color: var(--text-muted);
        }
        
        .toggle {
            width: 52px;
            height: 28px;
            background: var(--border-color);
            border-radius: 14px;
            position: relative;
            cursor: pointer;
            transition: background var(--transition-fast);
            flex-shrink: 0;
        }
        
        .toggle.active {
            background: var(--color-success);
        }
        
        .toggle-slider {
            position: absolute;
            top: 2px;
            left: 2px;
            width: 24px;
            height: 24px;
            background: white;
            border-radius: 50%;
            transition: left var(--transition-fast);
            box-shadow: var(--shadow-sm);
        }
        
        .toggle.active .toggle-slider {
            left: 26px;
        }
        
        .difficulty-options {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 0.5rem;
        }
        
        .difficulty-btn {
            padding: 0.875rem;
            border: 2px solid var(--border-color);
            border-radius: var(--radius-md);
            background: var(--bg-primary);
            color: var(--text-primary);
            font-weight: 600;
            cursor: pointer;
            text-align: center;
            transition: all var(--transition-fast);
            user-select: none;
        }
        
        .difficulty-btn:hover {
            background: var(--bg-tertiary);
        }
        
        .difficulty-btn.active {
            border-color: var(--color-primary);
            background: var(--color-primary);
            color: white;
            box-shadow: var(--shadow-md);
        }
        
        /* Loading */
        .loading {
            display: inline-block;
            width: 1rem;
            height: 1rem;
            border: 2px solid var(--border-color);
            border-radius: 50%;
            border-top-color: var(--color-primary);
            animation: spin 0.8s linear infinite;
        }
        
        @keyframes spin {
            to { transform: rotate(360deg); }
        }
        
        /* Responsive */
        @media (max-width: 640px) {
            .stats-grid {
                grid-template-columns: repeat(2, 1fr);
            }
            
            .detail-grid {
                grid-template-columns: repeat(2, 1fr);
            }
            
            .header-actions {
                width: 100%;
            }
            
            .btn {
                flex: 1;
            }
            
            .modal-content {
                padding: 1.5rem;
            }
        }
        
        /* Accessibility */
        .btn:focus-visible,
        .input-field:focus-visible,
        .search-input:focus-visible {
            outline: 2px solid var(--color-primary);
            outline-offset: 2px;
        }
        
        /* Smooth scrolling */
        html {
            scroll-behavior: smooth;
        }
        
        /* Performance optimizations */
        * {
            will-change: auto;
        }
        
        .stock-item,
        .btn,
        .tab,
        .modal {
            will-change: transform;
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- Header -->
        <header class="header">
            <div class="header-top">
                <div class="logo">
                    <span class="logo-icon">📊</span>
                    <span>BIST Trader Pro</span>
                </div>
                <div class="header-actions">
                    <button class="btn btn-secondary" onclick="app.toggleTheme()" id="themeBtn" aria-label="Tema değiştir">
                        🌙 Tema
                    </button>
                    <button class="btn btn-secondary" onclick="app.openSettings()" aria-label="Ayarlar">
                        ⚙️ Ayarlar
                    </button>
                    <button class="btn btn-danger" onclick="app.sellAll()" aria-label="Tümünü sat">
                        💸 Tümünü Sat
                    </button>
                    <button class="btn btn-secondary" onclick="app.resetGame()" aria-label="Oyunu sıfırla">
                        🔄 Sıfırla
                    </button>
                </div>
            </div>
            
            <div class="stats-grid">
                <div class="stat-card">
                    <div class="stat-label">💰 Nakit</div>
                    <div class="stat-value" id="cashValue">100.000 ₺</div>
                </div>
                <div class="stat-card">
                    <div class="stat-label">📊 Portföy</div>
                    <div class="stat-value" id="portfolioValue">0 ₺</div>
                </div>
                <div class="stat-card">
                    <div class="stat-label">💼 Toplam</div>
                    <div class="stat-value" id="totalValue">100.000 ₺</div>
                </div>
                <div class="stat-card">
                    <div class="stat-label">📈 Kar/Zarar</div>
                    <div class="stat-value" id="profitValue">0 ₺</div>
                    <div class="stat-change" id="profitChange">0.00%</div>
                </div>
            </div>
        </header>
        
        <!-- Navigation -->
        <nav class="tabs" role="tablist">
            <button class="tab active" role="tab" aria-selected="true" onclick="app.switchTab(0)">
                📊 Piyasa
            </button>
            <button class="tab" role="tab" aria-selected="false" onclick="app.switchTab(1)">
                💼 Portföy
            </button>
            <button class="tab" role="tab" aria-selected="false" onclick="app.switchTab(2)">
                📜 İşlem Geçmişi
            </button>
            <button class="tab" role="tab" aria-selected="false" onclick="app.switchTab(3)">
                ⭐ İzleme Listesi
            </button>
        </nav>
        
        <!-- Tab: Market -->
        <div class="tab-content active" id="tab0" role="tabpanel">
            <div class="main-grid">
                <div class="panel">
                    <div class="panel-header">
                        <h2 class="panel-title">BIST Hisseleri</h2>
                        <button class="btn btn-secondary btn-sm" onclick="app.sortStocks()">
                            🔄 Sırala
                        </button>
                    </div>
                    <div class="search-container">
                        <span class="search-icon">🔍</span>
                        <input 
                            type="text" 
                            id="searchInput" 
                            class="search-input" 
                            placeholder="Hisse ara..."
                            oninput="app.filterStocks()"
                            aria-label="Hisse ara"
                        >
                    </div>
                    <div class="stock-list" id="stockList"></div>
                </div>
                
                <div class="panel">
                    <h2 class="panel-title">Piyasa Özeti</h2>
                    <div class="stats-grid" style="margin-top: 1rem;">
                        <div class="stat-card">
                            <div class="stat-label">Toplam</div>
                            <div class="stat-value" id="totalStocks">18</div>
                        </div>
                        <div class="stat-card">
                            <div class="stat-label">Yükseliş</div>
                            <div class="stat-value text-success" id="risingStocks">0</div>
                        </div>
                        <div class="stat-card">
                            <div class="stat-label">Düşüş</div>
                            <div class="stat-value text-danger" id="fallingStocks">0</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        <!-- Tab: Portfolio -->
        <div class="tab-content" id="tab1" role="tabpanel">
            <div class="panel">
                <div class="panel-header">
                    <h2 class="panel-title">Portföy Detayı</h2>
                    <button class="btn btn-secondary btn-sm" onclick="app.exportPortfolio()">
                        📥 Dışa Aktar
                    </button>
                </div>
                <div class="stats-grid">
                    <div class="stat-card">
                        <div class="stat-label">Yatırım</div>
                        <div class="stat-value" id="totalInvested">0 ₺</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-label">Getiri</div>
                        <div class="stat-value" id="returnRate">0%</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-label">En İyi</div>
                        <div class="stat-value" id="bestStock">-</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-label">İşlemler</div>
                        <div class="stat-value" id="totalTrades">0</div>
                    </div>
                </div>
                <div class="chart-container">
                    <canvas id="portfolioChart" style="max-height: 300px;"></canvas>
                </div>
                <div id="portfolioList" style="margin-top: 1.5rem;"></div>
            </div>
        </div>
        
        <!-- Tab: History -->
        <div class="tab-content" id="tab2" role="tabpanel">
            <div class="panel">
                <div class="panel-header">
                    <h2 class="panel-title">İşlem Geçmişi</h2>
                    <button class="btn btn-danger btn-sm" onclick="app.clearHistory()">
                        🗑️ Temizle
                    </button>
                </div>
                <div id="historyList"></div>
            </div>
        </div>
        
        <!-- Tab: Watchlist -->
        <div class="tab-content" id="tab3" role="tabpanel">
            <div class="panel">
                <h2 class="panel-title">İzleme Listesi</h2>
                <div id="watchlistContent"></div>
            </div>
        </div>
    </div>
    
    <!-- Stock Modal -->
    <div class="modal" id="stockModal" role="dialog" aria-labelledby="modalTitle" aria-modal="true">
        <div class="modal-content">
            <div class="modal-header">
                <div>
                    <h2 class="modal-title" id="modalTitle"></h2>
                    <div class="modal-subtitle" id="modalSubtitle"></div>
                </div>
                <button class="btn btn-danger btn-sm" onclick="app.closeModal()" aria-label="Kapat">
                    ✕
                </button>
            </div>
            
            <div class="detail-grid">
                <div class="detail-card">
                    <div class="detail-label">Fiyat</div>
                    <div class="detail-value" id="detailPrice">0 ₺</div>
                </div>
                <div class="detail-card">
                    <div class="detail-label">Değişim</div>
                    <div class="detail-value" id="detailChange">0%</div>
                </div>
                <div class="detail-card">
                    <div class="detail-label">Sahip</div>
                    <div class="detail-value" id="detailOwned">0</div>
                </div>
                <div class="detail-card">
                    <div class="detail-label">Değer</div>
                    <div class="detail-value" id="detailValue">0 ₺</div>
                </div>
            </div>
            
            <div class="indicators-section">
                <div class="indicators-title">Teknik İndikatörler</div>
                <div class="indicators-grid">
                    <div class="indicator-item">
                        <div class="indicator-label">RSI (14)</div>
                        <div class="indicator-value" id="rsiValue">50</div>
                        <div class="indicator-signal signal-neutral" id="rsiSignal">Nötr</div>
                    </div>
                    <div class="indicator-item">
                        <div class="indicator-label">MACD</div>
                        <div class="indicator-value" id="macdValue">0</div>
                        <div class="indicator-signal signal-neutral" id="macdSignal">Nötr</div>
                    </div>
                    <div class="indicator-item">
                        <div class="indicator-label">MA (50)</div>
                        <div class="indicator-value" id="maValue">0</div>
                        <div class="indicator-signal signal-neutral" id="maSignal">Nötr</div>
                    </div>
                </div>
            </div>
            
            <div class="chart-container">
                <canvas id="detailChart" style="max-height: 250px;"></canvas>
            </div>
            
            <div class="trade-tabs">
                <button class="trade-tab active-buy" id="buyTab" onclick="app.switchTradeTab('buy')">
                    🛒 Satın Al
                </button>
                <button class="trade-tab" id="sellTab" onclick="app.switchTradeTab('sell')">
                    💸 Sat
                </button>
            </div>
            
            <div id="tradeSection">
                <div class="input-group">
                    <label class="input-label" for="tradeAmount">Miktar</label>
                    <input 
                        type="number" 
                        id="tradeAmount" 
                        class="input-field" 
                        value="1" 
                        min="1"
                        oninput="app.updateSummary()"
                        aria-label="İşlem miktarı"
                    >
                </div>
                
                <div class="quick-buttons">
                    <button class="quick-btn" onclick="app.setPercent(0.25)">25%</button>
                    <button class="quick-btn" onclick="app.setPercent(0.5)">50%</button>
                    <button class="quick-btn" onclick="app.setPercent(0.75)">75%</button>
                    <button class="quick-btn" onclick="app.setPercent(1)">MAX</button>
                </div>
                
                <div class="summary-box">
                    <div class="summary-row">
                        <span>Tutar:</span>
                        <strong id="summaryAmount">0 ₺</strong>
                    </div>
                    <div class="summary-row">
                        <span>Komisyon:</span>
                        <strong id="summaryCommission">0 ₺</strong>
                    </div>
                    <div class="summary-row">
                        <span>Toplam:</span>
                        <strong id="summaryTotal">0 ₺</strong>
                    </div>
                </div>
                
                <button 
                    class="btn btn-lg" 
                    id="tradeButton" 
                    style="width: 100%;" 
                    onclick="app.executeTrade()"
                >
                    🛒 Satın Al
                </button>
            </div>
        </div>
    </div>
    
    <!-- Settings Modal -->
    <div class="modal" id="settingsModal" role="dialog" aria-labelledby="settingsTitle" aria-modal="true">
        <div class="modal-content">
            <div class="modal-header">
                <h2 class="modal-title" id="settingsTitle">⚙️ Ayarlar</h2>
                <button class="btn btn-danger btn-sm" onclick="app.closeSettings()" aria-label="Kapat">
                    ✕
                </button>
            </div>
            
            <div class="settings-section">
                <h3 class="settings-section-title">Zorluk Seviyesi</h3>
                <div class="settings-item">
                    <div class="settings-info">
                        <p>Piyasa volatilitesini ayarlayın</p>
                    </div>
                </div>
                <div class="difficulty-options">
                    <button class="difficulty-btn" id="diffEasy" onclick="app.setDifficulty('easy')">
                        Kolay
                    </button>
                    <button class="difficulty-btn active" id="diffMedium" onclick="app.setDifficulty('medium')">
                        Orta
                    </button>
                    <button class="difficulty-btn" id="diffHard" onclick="app.setDifficulty('hard')">
                        Zor
                    </button>
                </div>
            </div>
            
            <div class="settings-section">
                <h3 class="settings-section-title">Tercihler</h3>
                <div class="settings-item">
                    <div class="settings-info">
                        <h4>Komisyon</h4>
                        <p>İşlem başına 0.2% komisyon</p>
                    </div>
                    <button 
                        class="toggle active" 
                        id="commissionToggle" 
                        onclick="app.toggleSetting('commission')"
                        role="switch"
                        aria-checked="true"
                        aria-label="Komisyon ayarı"
                    >
                        <div class="toggle-slider"></div>
                    </button>
                </div>
                
                <div class="settings-item">
                    <div class="settings-info">
                        <h4>Bildirimler</h4>
                        <p>İşlem bildirimlerini göster</p>
                    </div>
                    <button 
                        class="toggle active" 
                        id="notificationsToggle" 
                        onclick="app.toggleSetting('notifications')"
                        role="switch"
                        aria-checked="true"
                        aria-label="Bildirim ayarı"
                    >
                        <div class="toggle-slider"></div>
                    </button>
                </div>
            </div>
        </div>
    </div>
    
    <script>
        'use strict';
        
        // Application State
        const app = {
            // Constants
            COMMISSION_RATE: 0.002,
            INITIAL_CASH: 100000,
            
            // State
            cash: 100000,
            portfolio: {},
            tradeHistory: [],
            watchlist: [],
            selectedStock: null,
            tradeMode: 'buy',
            totalTrades: 0,
            difficulty: 'medium',
            settings: {
                commission: true,
                notifications: true
            },
            
            // Charts
            portfolioChart: null,
            detailChart: null,
            
            // Stock Data
            stocks: [
                {id:1,symbol:'THYAO',name:'Türk Hava Yolları',sector:'Ulaştırma',price:250.50,basePrice:250.50,history:[250.50],change:0},
                {id:2,symbol:'TUPRS',name:'Tüpraş',sector:'Enerji',price:180.75,basePrice:180.75,history:[180.75],change:0},
                {id:3,symbol:'AKBNK',name:'Akbank',sector:'Finans',price:45.30,basePrice:45.30,history:[45.30],change:0},
                {id:4,symbol:'BIMAS',name:'BIM',sector:'Perakende',price:320.20,basePrice:320.20,history:[320.20],change:0},
                {id:5,symbol:'EREGL',name:'Ereğli Demir Çelik',sector:'Metal',price:28.60,basePrice:28.60,history:[28.60],change:0},
                {id:6,symbol:'KCHOL',name:'Koç Holding',sector:'Holding',price:95.40,basePrice:95.40,history:[95.40],change:0},
                {id:7,symbol:'GARAN',name:'Garanti BBVA',sector:'Finans',price:68.50,basePrice:68.50,history:[68.50],change:0},
                {id:8,symbol:'SAHOL',name:'Sabancı Holding',sector:'Holding',price:52.80,basePrice:52.80,history:[52.80],change:0},
                {id:9,symbol:'ASELS',name:'Aselsan',sector:'Savunma',price:142.90,basePrice:142.90,history:[142.90],change:0},
                {id:10,symbol:'SISE',name:'Şişe Cam',sector:'Sanayi',price:38.70,basePrice:38.70,history:[38.70],change:0},
                {id:11,symbol:'TCELL',name:'Turkcell',sector:'Telekomünikasyon',price:78.20,basePrice:78.20,history:[78.20],change:0},
                {id:12,symbol:'PETKM',name:'Petkim',sector:'Kimya',price:15.45,basePrice:15.45,history:[15.45],change:0},
                {id:13,symbol:'KOZAL',name:'Koza Altın',sector:'Madencilik',price:89.30,basePrice:89.30,history:[89.30],change:0},
                {id:14,symbol:'DOHOL',name:'Doğan Holding',sector:'Holding',price:12.85,basePrice:12.85,history:[12.85],change:0},
                {id:15,symbol:'TOASO',name:'Tofaş',sector:'Otomotiv',price:105.60,basePrice:105.60,history:[105.60],change:0},
                {id:16,symbol:'VESTL',name:'Vestel',sector:'Teknoloji',price:24.30,basePrice:24.30,history:[24.30],change:0},
                {id:17,symbol:'HALKB',name:'Halkbank',sector:'Finans',price:35.80,basePrice:35.80,history:[35.80],change:0},
                {id:18,symbol:'ISCTR',name:'İş Bankası',sector:'Finans',price:48.90,basePrice:48.90,history:[48.90],change:0}
            ],
            
            // Utility Functions
            formatMoney(amount) {
                return new Intl.NumberFormat('tr-TR', {
                    style: 'currency',
                    currency: 'TRY',
                    minimumFractionDigits: 0,
                    maximumFractionDigits: 0
                }).format(amount);
            },
            
            showNotification(message, type = 'success') {
                if (!this.settings.notifications) return;
                
                const icons = {
                    success: '✅',
                    error: '❌',
                    warning: '⚠️',
                    info: 'ℹ️'
                };
                
                const notification = document.createElement('div');
                notification.className = `notification ${type}`;
                notification.innerHTML = `
                    <div class="notification-icon">${icons[type] || icons.info}</div>
                    <div class="notification-text">${message}</div>
                `;
                document.body.appendChild(notification);
                
                setTimeout(() => notification.remove(), 3000);
            },
            
            // Technical Indicators
            calculateRSI(prices, period = 14) {
                if (prices.length < period + 1) return 50;
                
                let gains = 0;
                let losses = 0;
                
                for (let i = prices.length - period; i < prices.length; i++) {
                    const change = prices[i] - prices[i - 1];
                    if (change > 0) gains += change;
                    else losses += Math.abs(change);
                }
                
                const avgGain = gains / period;
                const avgLoss = losses / period;
                
                if (avgLoss === 0) return 100;
                const rs = avgGain / avgLoss;
                return 100 - (100 / (1 + rs));
            },
            
            calculateMA(prices, period = 50) {
                if (prices.length < period) return prices[prices.length - 1];
                const slice = prices.slice(-period);
                return slice.reduce((a, b) => a + b, 0) / period;
            },
            
            calculateMACD(prices) {
                if (prices.length < 26) return 0;
                const ema12 = this.calculateEMA(prices, 12);
                const ema26 = this.calculateEMA(prices, 26);
                return ema12 - ema26;
            },
            
            calculateEMA(prices, period) {
                const k = 2 / (period + 1);
                let ema = prices[Math.max(0, prices.length - period)];
                for (let i = Math.max(0, prices.length - period + 1); i < prices.length; i++) {
                    ema = prices[i] * k + ema * (1 - k);
                }
                return ema;
            },
            
            // Stock Functions
            filterStocks() {
                const search = document.getElementById('searchInput').value.toUpperCase();
                document.querySelectorAll('.stock-item').forEach(el => {
                    const text = el.textContent.toUpperCase();
                    el.style.display = text.includes(search) ? '' : 'none';
                });
            },
            
            sortStocks() {
                this.stocks.sort((a, b) => Math.abs(b.change) - Math.abs(a.change));
                this.renderStocks();
            },
            
            renderStocks() {
                const list = document.getElementById('stockList');
                let rising = 0, falling = 0;
                
                list.innerHTML = this.stocks.map(stock => {
                    if (stock.change > 0) rising++;
                    if (stock.change < 0) falling++;
                    
                    const isWatched = this.watchlist.includes(stock.id);
                    const changeClass = stock.change >= 0 ? 'text-success' : 'text-danger';
                    const changeIcon = stock.change >= 0 ? '▲' : '▼';
                    
                    return `
                        <div class="stock-item" onclick="app.openStock(${stock.id})">
                            <button 
                                class="watchlist-btn ${isWatched ? 'active' : ''}" 
                                onclick="event.stopPropagation(); app.toggleWatchlist(${stock.id})"
                                aria-label="${isWatched ? 'İzleme listesinden çıkar' : 'İzleme listesine ekle'}"
                            >
                                ${isWatched ? '⭐' : '☆'}
                            </button>
                            <div class="stock-header">
                                <div class="stock-info">
                                    <div class="stock-symbol">${stock.symbol}</div>
                                    <div class="stock-name">${stock.name}</div>
                                </div>
                                <div class="stock-price-info">
                                    <div class="stock-price">${this.formatMoney(stock.price)}</div>
                                    <div class="stock-change ${changeClass}">
                                        <span>${changeIcon}</span>
                                        <span>${Math.abs(stock.change).toFixed(2)}%</span>
                                    </div>
                                </div>
                            </div>
                            <div class="stock-meta">
                                <div class="stock-meta-item">
                                    <span>${stock.sector}</span>
                                </div>
                            </div>
                        </div>
                    `;
                }).join('');
                
                document.getElementById('risingStocks').textContent = rising;
                document.getElementById('fallingStocks').textContent = falling;
            },
            
            toggleWatchlist(stockId) {
                const index = this.watchlist.indexOf(stockId);
                if (index === -1) {
                    this.watchlist.push(stockId);
                    this.showNotification('İzleme listesine eklendi');
                } else {
                    this.watchlist.splice(index, 1);
                    this.showNotification('İzleme listesinden çıkarıldı', 'info');
                }
                this.renderStocks();
                this.renderWatchlist();
                this.saveData();
            },
            
            renderWatchlist() {
                const content = document.getElementById('watchlistContent');
                
                if (this.watchlist.length === 0) {
                    content.innerHTML = `
                        <div class="empty-state">
                            <div class="empty-icon">⭐</div>
                            <div class="empty-text">İzleme listeniz boş</div>
                        </div>
                    `;
                    return;
                }
                
                content.innerHTML = this.watchlist.map(id => {
                    const stock = this.stocks.find(s => s.id === id);
                    if (!stock) return '';
                    
                    const changeClass = stock.change >= 0 ? 'text-success' : 'text-danger';
                    const changeIcon = stock.change >= 0 ? '▲' : '▼';
                    
                    return `
                        <div class="stock-item" onclick="app.openStock(${stock.id})">
                            <button 
                                class="watchlist-btn active" 
                                onclick="event.stopPropagation(); app.toggleWatchlist(${stock.id})"
                                aria-label="İzleme listesinden çıkar"
                            >
                                ⭐
                            </button>
                            <div class="stock-header">
                                <div class="stock-info">
                                    <div class="stock-symbol">${stock.symbol}</div>
                                    <div class="stock-name">${stock.name}</div>
                                </div>
                                <div class="stock-price-info">
                                    <div class="stock-price">${this.formatMoney(stock.price)}</div>
                                    <div class="stock-change ${changeClass}">
                                        <span>${changeIcon}</span>
                                        <span>${Math.abs(stock.change).toFixed(2)}%</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    `;
                }).join('');
            },
            
            // Portfolio Functions
            renderPortfolio() {
                const list = document.getElementById('portfolioList');
                const items = Object.entries(this.portfolio);
                
                if (items.length === 0) {
                    list.innerHTML = `
                        <div class="empty-state">
                            <div class="empty-icon">💼</div>
                            <div class="empty-text">Portföyünüzde hisse yok</div>
                        </div>
                    `;
                    this.updatePortfolioChart();
                    return;
                }
                
                let totalInv = 0;
                let bestProfit = -Infinity;
                let bestSymbol = '-';
                
                list.innerHTML = items.map(([id, data]) => {
                    const stock = this.stocks.find(s => s.id == id);
                    const currentValue = stock.price * data.amount;
                    const profit = currentValue - data.invested;
                    const profitPct = ((profit / data.invested) * 100).toFixed(2);
                    
                    totalInv += data.invested;
                    if (profit > bestProfit) {
                        bestProfit = profit;
                        bestSymbol = stock.symbol;
                    }
                    
                    const profitClass = profit >= 0 ? 'text-success' : 'text-danger';
                    
                    return `
                        <div class="stock-item" onclick="app.openStock(${id})">
                            <div class="stock-header">
                                <div class="stock-info">
                                    <div class="stock-symbol">${stock.symbol}</div>
                                    <div class="stock-name">${data.amount} adet • Ort: ${this.formatMoney(data.avgPrice)}</div>
                                </div>
                                <div class="stock-price-info">
                                    <div class="stock-price ${profitClass}">${this.formatMoney(currentValue)}</div>
                                    <div class="stock-change ${profitClass}">
                                        ${profit >= 0 ? '+' : ''}${this.formatMoney(profit)} (${profitPct}%)
                                    </div>
                                </div>
                            </div>
                        </div>
                    `;
                }).join('');
                
                const portfolioVal = items.reduce((sum, [id, data]) => {
                    const stock = this.stocks.find(s => s.id == id);
                    return sum + stock.price * data.amount;
                }, 0);
                
                const returnRate = totalInv > 0 ? ((portfolioVal - totalInv) / totalInv * 100).toFixed(2) : '0.00';
                
                document.getElementById('totalInvested').textContent = this.formatMoney(totalInv);
                document.getElementById('returnRate').textContent = returnRate + '%';
                document.getElementById('bestStock').textContent = bestSymbol;
                document.getElementById('totalTrades').textContent = this.totalTrades;
                
                this.updatePortfolioChart();
            },
            
            updatePortfolioChart() {
                const canvas = document.getElementById('portfolioChart');
                if (!canvas) return;
                
                if (this.portfolioChart) {
                    this.portfolioChart.destroy();
                    this.portfolioChart = null;
                }
                
                const items = Object.entries(this.portfolio);
                if (items.length === 0) return;
                
                const theme = document.body.getAttribute('data-theme');
                const textColor = theme === 'light' ? '#0f172a' : '#f8fafc';
                
                this.portfolioChart = new Chart(canvas, {
                    type: 'doughnut',
                    data: {
                        labels: items.map(([id]) => this.stocks.find(s => s.id == id).symbol),
                        datasets: [{
                            data: items.map(([id, portData]) => {
                                const stock = this.stocks.find(s => s.id == id);
                                return stock.price * portData.amount;
                            }),
                            backgroundColor: [
                                '#0ea5e9', '#22c55e', '#f59e0b', '#ef4444',
                                '#8b5cf6', '#06b6d4', '#ec4899', '#14b8a6',
                                '#f97316', '#a855f7', '#84cc16', '#f43f5e'
                            ]
                        }]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: true,
                        plugins: {
                            legend: {
                                position: 'bottom',
                                labels: {
                                    color: textColor,
                                    padding: 15,
                                    font: { size: 12 }
                                }
                            }
                        }
                    }
                });
            },
            
            // History Functions
            renderHistory() {
                const list = document.getElementById('historyList');
                
                if (this.tradeHistory.length === 0) {
                    list.innerHTML = `
                        <div class="empty-state">
                            <div class="empty-icon">📜</div>
                            <div class="empty-text">İşlem geçmişiniz boş</div>
                        </div>
                    `;
                    return;
                }
                
                list.innerHTML = this.tradeHistory.slice(0, 50).map(trade => `
                    <div class="history-item">
                        <div>
                            <div class="history-badge ${trade.type === 'buy' ? 'badge-buy' : 'badge-sell'}">
                                ${trade.type === 'buy' ? 'ALIŞ' : 'SATIŞ'}
                            </div>
                            <div class="font-semibold">${trade.symbol}</div>
                            <div class="text-sm text-muted">${trade.time}</div>
                        </div>
                        <div style="text-align: right;">
                            <div class="font-semibold">${trade.amount} adet</div>
                            <div class="text-sm text-muted">${this.formatMoney(trade.price)}</div>
                            <div class="font-bold">${this.formatMoney(trade.total)}</div>
                        </div>
                    </div>
                `).join('');
            },
            
            clearHistory() {
                if (!confirm('İşlem geçmişini silmek istediğinizden emin misiniz?')) return;
                this.tradeHistory = [];
                this.renderHistory();
                this.saveData();
                this.showNotification('İşlem geçmişi temizlendi');
            },
            
            exportPortfolio() {
                const items = Object.entries(this.portfolio);
                if (items.length === 0) {
                    this.showNotification('Portföyünüz boş', 'error');
                    return;
                }
                
                let csv = 'Hisse,Miktar,Ort. Fiyat,Yatırım,Güncel Fiyat,Güncel Değer,Kar/Zarar\n';
                
                items.forEach(([id, data]) => {
                    const stock = this.stocks.find(s => s.id == id);
                    const currentValue = stock.price * data.amount;
                    const profit = currentValue - data.invested;
                    csv += `${stock.symbol},${data.amount},${data.avgPrice},${data.invested},${stock.price},${currentValue},${profit}\n`;
                });
                
                const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
                const url = URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.href = url;
                a.download = `portfoy_${Date.now()}.csv`;
                a.click();
                URL.revokeObjectURL(url);
                this.showNotification('Portföy dışa aktarıldı');
            },
            
            // Modal Functions
            openStock(stockId) {
                this.selectedStock = this.stocks.find(s => s.id === stockId);
                if (!this.selectedStock) return;
                
                const owned = this.portfolio[stockId] ? this.portfolio[stockId].amount : 0;
                const value = this.selectedStock.price * owned;
                
                document.getElementById('modalTitle').textContent = this.selectedStock.symbol;
                document.getElementById('modalSubtitle').textContent = `${this.selectedStock.name} • ${this.selectedStock.sector}`;
                document.getElementById('detailPrice').textContent = this.formatMoney(this.selectedStock.price);
                
                const changeClass = this.selectedStock.change >= 0 ? 'text-success' : 'text-danger';
                const changeIcon = this.selectedStock.change >= 0 ? '▲' : '▼';
                const changeEl = document.getElementById('detailChange');
                changeEl.textContent = `${changeIcon} ${Math.abs(this.selectedStock.change).toFixed(2)}%`;
                changeEl.className = `detail-value ${changeClass}`;
                
                document.getElementById('detailOwned').textContent = owned;
                document.getElementById('detailValue').textContent = this.formatMoney(value);
                
                this.updateIndicators();
                this.drawDetailChart();
                this.switchTradeTab('buy');
                
                document.getElementById('stockModal').classList.add('active');
                document.body.style.overflow = 'hidden';
            },
            
            closeModal() {
                document.getElementById('stockModal').classList.remove('active');
                document.body.style.overflow = '';
            },
            
            updateIndicators() {
                const rsi = this.calculateRSI(this.selectedStock.history);
                const macd = this.calculateMACD(this.selectedStock.history);
                const ma = this.calculateMA(this.selectedStock.history, 50);
                
                document.getElementById('rsiValue').textContent = rsi.toFixed(1);
                const rsiSignal = document.getElementById('rsiSignal');
                if (rsi < 30) {
                    rsiSignal.textContent = 'Aşırı Satım';
                    rsiSignal.className = 'indicator-signal signal-buy';
                } else if (rsi > 70) {
                    rsiSignal.textContent = 'Aşırı Alım';
                    rsiSignal.className = 'indicator-signal signal-sell';
                } else {
                    rsiSignal.textContent = 'Nötr';
                    rsiSignal.className = 'indicator-signal signal-neutral';
                }
                
                document.getElementById('macdValue').textContent = macd.toFixed(2);
                const macdSignal = document.getElementById('macdSignal');
                if (macd > 0) {
                    macdSignal.textContent = 'Alış';
                    macdSignal.className = 'indicator-signal signal-buy';
                } else {
                    macdSignal.textContent = 'Satış';
                    macdSignal.className = 'indicator-signal signal-sell';
                }
                
                document.getElementById('maValue').textContent = this.formatMoney(ma);
                const maSignal = document.getElementById('maSignal');
                if (this.selectedStock.price > ma) {
                    maSignal.textContent = 'Yukarı';
                    maSignal.className = 'indicator-signal signal-buy';
                } else {
                    maSignal.textContent = 'Aşağı';
                    maSignal.className = 'indicator-signal signal-sell';
                }
            },
            
            drawDetailChart() {
                const canvas = document.getElementById('detailChart');
                if (!canvas) return;
                
                if (this.detailChart) {
                    this.detailChart.destroy();
                }
                
                const theme = document.body.getAttribute('data-theme');
                const textColor = theme === 'light' ? '#64748b' : '#94a3b8';
                const borderColor = theme === 'light' ? '#e2e8f0' : '#334155';
                
                this.detailChart = new Chart(canvas, {
                    type: 'line',
                    data: {
                        labels: this.selectedStock.history.map(() => ''),
                        datasets: [{
                            data: this.selectedStock.history,
                            borderColor: '#0ea5e9',
                            backgroundColor: 'rgba(14, 165, 233, 0.1)',
                            borderWidth: 2,
                            fill: true,
                            tension: 0.4,
                            pointRadius: 0,
                            pointHoverRadius: 5
                        }]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: true,
                        plugins: {
                            legend: { display: false },
                            tooltip: {
                                callbacks: {
                                    label: (ctx) => 'Fiyat: ' + this.formatMoney(ctx.parsed.y)
                                }
                            }
                        },
                        scales: {
                            y: {
                                ticks: {
                                    callback: (value) => this.formatMoney(value),
                                    color: textColor
                                },
                                grid: {
                                    color: borderColor
                                }
                            },
                            x: {
                                display: false
                            }
                        }
                    }
                });
            },
            
            switchTradeTab(mode) {
                this.tradeMode = mode;
                const buyTab = document.getElementById('buyTab');
                const sellTab = document.getElementById('sellTab');
                const button = document.getElementById('tradeButton');
                
                if (mode === 'buy') {
                    buyTab.className = 'trade-tab active-buy';
                    sellTab.className = 'trade-tab';
                    button.textContent = '🛒 Satın Al';
                    button.className = 'btn btn-success btn-lg';
                } else {
                    buyTab.className = 'trade-tab';
                    sellTab.className = 'trade-tab active-sell';
                    button.textContent = '💸 Sat';
                    button.className = 'btn btn-danger btn-lg';
                }
                
                document.getElementById('tradeAmount').value = 1;
                this.updateSummary();
            },
            
            setPercent(percent) {
                const commRate = this.settings.commission ? this.COMMISSION_RATE : 0;
                
                if (this.tradeMode === 'buy') {
                    const available = this.cash * percent;
                    const maxAmount = Math.floor(available / (this.selectedStock.price * (1 + commRate)));
                    document.getElementById('tradeAmount').value = Math.max(1, maxAmount);
                } else {
                    const owned = this.portfolio[this.selectedStock.id] ? this.portfolio[this.selectedStock.id].amount : 0;
                    const amount = Math.floor(owned * percent);
                    document.getElementById('tradeAmount').value = Math.max(0, amount);
                }
                
                this.updateSummary();
            },
            
            updateSummary() {
                const amount = parseInt(document.getElementById('tradeAmount').value) || 0;
                const commRate = this.settings.commission ? this.COMMISSION_RATE : 0;
                const price = this.selectedStock.price * amount;
                const commission = price * commRate;
                const total = price + commission;
                
                document.getElementById('summaryAmount').textContent = this.formatMoney(price);
                document.getElementById('summaryCommission').textContent = this.formatMoney(commission);
                document.getElementById('summaryTotal').textContent = this.formatMoney(total);
            },
            
            executeTrade() {
                const amount = parseInt(document.getElementById('tradeAmount').value) || 0;
                
                if (amount < 1) {
                    this.showNotification('Miktar en az 1 olmalı', 'error');
                    return;
                }
                
                const commRate = this.settings.commission ? this.COMMISSION_RATE : 0;
                
                if (this.tradeMode === 'buy') {
                    const cost = this.selectedStock.price * amount;
                    const commission = cost * commRate;
                    const total = cost + commission;
                    
                    if (total > this.cash) {
                        this.showNotification('Yetersiz bakiye', 'error');
                        return;
                    }
                    
                    this.cash -= total;
                    
                    if (!this.portfolio[this.selectedStock.id]) {
                        this.portfolio[this.selectedStock.id] = { amount: 0, avgPrice: 0, invested: 0 };
                    }
                    
                    const port = this.portfolio[this.selectedStock.id];
                    const oldValue = port.amount * port.avgPrice;
                    port.amount += amount;
                    port.invested += cost;
                    port.avgPrice = (oldValue + cost) / port.amount;
                    
                    this.tradeHistory.unshift({
                        type: 'buy',
                        symbol: this.selectedStock.symbol,
                        amount: amount,
                        price: this.selectedStock.price,
                        total: total,
                        time: new Date().toLocaleString('tr-TR')
                    });
                    
                    this.totalTrades++;
                    this.showNotification(`${amount} adet ${this.selectedStock.symbol} alındı`);
                    
                } else {
                    if (!this.portfolio[this.selectedStock.id] || this.portfolio[this.selectedStock.id].amount < amount) {
                        this.showNotification('Yeterli hisse yok', 'error');
                        return;
                    }
                    
                    const value = this.selectedStock.price * amount;
                    const commission = value * commRate;
                    const net = value - commission;
                    
                    this.cash += net;
                    
                    const port = this.portfolio[this.selectedStock.id];
                    const ratio = amount / port.amount;
                    port.invested -= port.invested * ratio;
                    port.amount -= amount;
                    
                    if (port.amount === 0) {
                        delete this.portfolio[this.selectedStock.id];
                    }
                    
                    this.tradeHistory.unshift({
                        type: 'sell',
                        symbol: this.selectedStock.symbol,
                        amount: amount,
                        price: this.selectedStock.price,
                        total: net,
                        time: new Date().toLocaleString('tr-TR')
                    });
                    
                    this.totalTrades++;
                    this.showNotification(`${amount} adet ${this.selectedStock.symbol} satıldı`);
                }
                
                this.updateDisplay();
                this.closeModal();
                this.saveData();
            },
            
            sellAll() {
                const items = Object.keys(this.portfolio);
                if (items.length === 0) {
                    this.showNotification('Portföyünüzde hisse yok', 'error');
                    return;
                }
                
                if (!confirm('Tüm hisseleri satmak istediğinizden emin misiniz?')) return;
                
                const commRate = this.settings.commission ? this.COMMISSION_RATE : 0;
                let totalValue = 0;
                
                items.forEach(id => {
                    const stock = this.stocks.find(s => s.id == id);
                    const port = this.portfolio[id];
                    const value = stock.price * port.amount;
                    const commission = value * commRate;
                    const net = value - commission;
                    
                    this.cash += net;
                    totalValue += net;
                    
                    this.tradeHistory.unshift({
                        type: 'sell',
                        symbol: stock.symbol,
                        amount: port.amount,
                        price: stock.price,
                        total: net,
                        time: new Date().toLocaleString('tr-TR')
                    });
                    
                    this.totalTrades++;
                });
                
                this.portfolio = {};
                this.showNotification(`Tüm hisseler satıldı: ${this.formatMoney(totalValue)}`);
                this.updateDisplay();
                this.saveData();
            },
            
            // Settings
            openSettings() {
                document.getElementById('settingsModal').classList.add('active');
                document.body.style.overflow = 'hidden';
            },
            
            closeSettings() {
                document.getElementById('settingsModal').classList.remove('active');
                document.body.style.overflow = '';
            },
            
            setDifficulty(level) {
                this.difficulty = level;
                document.querySelectorAll('.difficulty-btn').forEach(btn => btn.classList.remove('active'));
                document.getElementById('diff' + level.charAt(0).toUpperCase() + level.slice(1)).classList.add('active');
                this.saveData();
                this.showNotification(`Zorluk: ${level === 'easy' ? 'Kolay' : level === 'medium' ? 'Orta' : 'Zor'}`);
            },
            
            toggleSetting(setting) {
                this.settings[setting] = !this.settings[setting];
                const toggle = document.getElementById(setting + 'Toggle');
                toggle.classList.toggle('active');
                toggle.setAttribute('aria-checked', this.settings[setting]);
                this.saveData();
                this.showNotification(`${setting === 'commission' ? 'Komisyon' : 'Bildirimler'}: ${this.settings[setting] ? 'Açık' : 'Kapalı'}`);
            },
            
            // Theme
            toggleTheme() {
                const currentTheme = document.body.getAttribute('data-theme');
                const newTheme = currentTheme === 'light' ? 'dark' : 'light';
                document.body.setAttribute('data-theme', newTheme);
                document.getElementById('themeBtn').textContent = newTheme === 'light' ? '☀️ Tema' : '🌙 Tema';
                
                // Update charts
                if (this.portfolioChart) this.updatePortfolioChart();
                if (this.detailChart) this.drawDetailChart();
                
                this.saveData();
            },
            
            // Tab Switching
            switchTab(index) {
                document.querySelectorAll('.tab').forEach((tab, i) => {
                    const isActive = i === index;
                    tab.classList.toggle('active', isActive);
                    tab.setAttribute('aria-selected', isActive);
                });
                document.querySelectorAll('.tab-content').forEach((content, i) => {
                    content.classList.toggle('active', i === index);
                });
            },
            
            // Update Display
            updateDisplay() {
                let portfolioValue = 0;
                Object.entries(this.portfolio).forEach(([id, data]) => {
                    const stock = this.stocks.find(s => s.id == id);
                    portfolioValue += stock.price * data.amount;
                });
                
                const totalValue = this.cash + portfolioValue;
                const profit = totalValue - this.INITIAL_CASH;
                const profitPercent = ((profit / this.INITIAL_CASH) * 100).toFixed(2);
                
                document.getElementById('cashValue').textContent = this.formatMoney(this.cash);
                document.getElementById('portfolioValue').textContent = this.formatMoney(portfolioValue);
                document.getElementById('totalValue').textContent = this.formatMoney(totalValue);
                document.getElementById('profitValue').textContent = this.formatMoney(profit);
                document.getElementById('profitChange').textContent = (profit >= 0 ? '+' : '') + profitPercent + '%';
                
                const profitEl = document.getElementById('profitValue');
                const changeEl = document.getElementById('profitChange');
                const profitClass = profit >= 0 ? 'text-success' : 'text-danger';
                profitEl.className = `stat-value ${profitClass}`;
                changeEl.className = `stat-change ${profitClass}`;
                
                this.renderStocks();
                this.renderPortfolio();
                this.renderHistory();
                this.renderWatchlist();
            },
            
            // Update Prices
            updatePrices() {
                const volatility = {
                    easy: 0.5,
                    medium: 1,
                    hard: 1.5
                }[this.difficulty];
                
                this.stocks.forEach(stock => {
                    const changePercent = (Math.random() - 0.5) * 5 * volatility;
                    stock.change = changePercent;
                    stock.price = Math.max(1, stock.price * (1 + changePercent / 100));
                    stock.history.push(stock.price);
                    if (stock.history.length > 100) stock.history.shift();
                });
                
                this.updateDisplay();
            },
            
            // Reset Game
            resetGame() {
                if (!confirm('Oyunu sıfırlamak istediğinizden emin misiniz? Tüm verileriniz silinecek!')) return;
                
                this.cash = this.INITIAL_CASH;
                this.portfolio = {};
                this.tradeHistory = [];
                this.totalTrades = 0;
                this.watchlist = [];
                
                this.stocks.forEach(stock => {
                    stock.price = stock.basePrice;
                    stock.history = [stock.basePrice];
                    stock.change = 0;
                });
                
                localStorage.removeItem('bistTraderPro');
                this.updateDisplay();
                this.showNotification('Oyun sıfırlandı');
            },
            
            // Data Persistence
            saveData() {
                try {
                    const data = {
                        cash: this.cash,
                        portfolio: this.portfolio,
                        tradeHistory: this.tradeHistory,
                        totalTrades: this.totalTrades,
                        watchlist: this.watchlist,
                        difficulty: this.difficulty,
                        settings: this.settings,
                        theme: document.body.getAttribute('data-theme')
                    };
                    localStorage.setItem('bistTraderPro', JSON.stringify(data));
                } catch (e) {
                    console.error('Save error:', e);
                }
            },
            
            loadData() {
                try {
                    const saved = localStorage.getItem('bistTraderPro');
                    if (saved) {
                        const data = JSON.parse(saved);
                        this.cash = data.cash || this.INITIAL_CASH;
                        this.portfolio = data.portfolio || {};
                        this.tradeHistory = data.tradeHistory || [];
                        this.totalTrades = data.totalTrades || 0;
                        this.watchlist = data.watchlist || [];
                        this.difficulty = data.difficulty || 'medium';
                        this.settings = data.settings || { commission: true, notifications: true };
                        
                        if (data.theme === 'light') {
                            document.body.setAttribute('data-theme', 'light');
                            document.getElementById('themeBtn').textContent = '☀️ Tema';
                        }
                        
                        this.setDifficulty(this.difficulty);
                        if (!this.settings.commission) {
                            document.getElementById('commissionToggle').classList.remove('active');
                            document.getElementById('commissionToggle').setAttribute('aria-checked', 'false');
                        }
                        if (!this.settings.notifications) {
                            document.getElementById('notificationsToggle').classList.remove('active');
                            document.getElementById('notificationsToggle').setAttribute('aria-checked', 'false');
                        }
                    }
                } catch (e) {
                    console.error('Load error:', e);
                }
            },
            
            // Initialize
            init() {
                this.loadData();
                this.updateDisplay();
                
                // Start price updates
                setInterval(() => this.updatePrices(), 3000);
                
                // Auto-save
                setInterval(() => this.saveData(), 30000);
                
                // Close modals on outside click
                document.addEventListener('click', (e) => {
                    if (e.target.classList.contains('modal')) {
                        e.target.classList.remove('active');
                        document.body.style.overflow = '';
                    }
                });
                
                // Keyboard shortcuts
                document.addEventListener('keydown', (e) => {
                    if (e.key === 'Escape') {
                        document.querySelectorAll('.modal').forEach(m => {
                            m.classList.remove('active');
                            document.body.style.overflow = '';
                        });
                    }
                });
                
                console.log('BIST Trader Pro initialized');
            }
        };
        
        // Start application
        document.addEventListener('DOMContentLoaded', () => app.init());
    </script>
</body>
</html>
