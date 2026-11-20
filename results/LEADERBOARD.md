# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 2:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 939 windows, 25970 settled trades, 67 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 477 | 35.0 | 34.8 | $-165.74 | -3.5% | $834.26 | -0.6 | done | can't tell from luck |
| value_ev10 | 1175 | 38.0 | 39.1 | $-679.43 | -5.8% | $320.57 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 2654 | 51.0 | 50.6 | $-877.46 | -3.3% | $122.54 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 2219 | 50.2 | 49.9 | $-913.22 | -4.1% | $86.78 | -1.9 | done | can't tell from luck |
| trend_filter | 1543 | 50.0 | 51.0 | $-1058.97 | -6.9% | $-58.97 | -2.8 | done | losing for real |
| value_ev5 | 1785 | 39.7 | 41.0 | $-1135.93 | -6.4% | $-135.93 | -2.3 | done | losing for real |
| coinflip | 3748 | 50.4 | 50.4 | $-1568.51 | -4.2% | $-568.51 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 2219 | 49.8 | 50.9 | $-1575.45 | -7.1% | $-575.45 | -3.4 | done | losing for real |
| momentum_15m_0.10pct | 2654 | 49.0 | 50.3 | $-1731.87 | -6.5% | $-731.87 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 3748 | 51.0 | 51.6 | $-1931.89 | -5.2% | $-931.89 | -3.3 | done | losing for real |
| always_up | 3748 | 46.7 | 49.7 | $-3836.77 | -10.2% | $-2836.77 | -6.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5919 | 48.2 | 49.1 | $-3475.55 |
| ETH | 6457 | 48.2 | 48.6 | $-4031.72 |
| SOL | 6773 | 48.2 | 48.6 | $-3975.83 |
| XRP | 6821 | 48.3 | 48.5 | $-3992.15 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
