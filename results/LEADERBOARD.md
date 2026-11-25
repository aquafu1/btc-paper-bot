# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 25, 6:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1386 windows, 35897 settled trades, 385 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 722 | 34.6 | 35.3 | $-497.54 | -6.9% | $502.46 | -1.4 | done | can't tell from luck |
| value_ev10 | 1744 | 38.8 | 39.2 | $-776.59 | -4.5% | $223.41 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 3584 | 50.8 | 50.1 | $-1045.31 | -2.9% | $-45.31 | -1.7 | done | can't tell from luck |
| value_ev5 | 2625 | 40.5 | 41.1 | $-1283.10 | -4.9% | $-283.10 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 3009 | 49.3 | 49.3 | $-1491.77 | -5.0% | $-491.77 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 3009 | 50.7 | 50.9 | $-1540.91 | -5.1% | $-540.91 | -2.9 | done | losing for real |
| trend_filter | 2131 | 48.5 | 50.4 | $-1887.49 | -8.9% | $-887.49 | -4.2 | done | losing for real |
| momentum_15m_0.10pct | 3584 | 49.2 | 50.2 | $-2199.81 | -6.1% | $-1199.81 | -3.7 | done | losing for real |
| coinflip | 5163 | 50.0 | 50.0 | $-2209.27 | -4.3% | $-1209.27 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 5163 | 50.1 | 51.3 | $-3201.21 | -6.2% | $-2201.21 | -4.6 | done | losing for real |
| always_up | 5163 | 47.9 | 49.3 | $-3727.74 | -7.2% | $-2727.74 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8959 | 48.0 | 48.8 | $-5041.51 |
| ETH | 9628 | 48.0 | 48.1 | $-5235.00 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
