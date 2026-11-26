# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 26, 8:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1491 windows, 37316 settled trades, 345 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 758 | 34.3 | 35.4 | $-583.02 | -7.7% | $416.98 | -1.6 | done | can't tell from luck |
| value_ev10 | 1820 | 38.5 | 39.2 | $-974.96 | -5.4% | $25.04 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 3711 | 50.9 | 50.1 | $-1020.10 | -2.7% | $-20.10 | -1.7 | done | can't tell from luck |
| value_ev5 | 2744 | 40.5 | 41.1 | $-1415.54 | -5.2% | $-415.54 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 3119 | 51.0 | 51.0 | $-1497.24 | -4.8% | $-497.24 | -2.7 | done | losing for real |
| momentum_60m_0.30pct | 3119 | 49.0 | 49.2 | $-1636.15 | -5.2% | $-636.15 | -2.9 | done | losing for real |
| trend_filter | 2215 | 48.5 | 50.3 | $-1923.16 | -8.7% | $-923.16 | -4.2 | done | losing for real |
| momentum_15m_0.10pct | 3711 | 49.1 | 50.2 | $-2257.93 | -6.1% | $-1257.93 | -3.7 | done | losing for real |
| coinflip | 5373 | 50.0 | 50.0 | $-2355.45 | -4.4% | $-1355.45 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 5373 | 50.1 | 51.3 | $-3379.02 | -6.3% | $-2379.02 | -4.7 | done | losing for real |
| always_up | 5373 | 48.0 | 49.2 | $-3609.23 | -6.7% | $-2609.23 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9639 | 48.0 | 48.7 | $-5390.81 |
| ETH | 10367 | 48.0 | 47.9 | $-5676.74 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
