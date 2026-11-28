# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 28, 3:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1660 windows, 39490 settled trades, 371 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 842 | 34.3 | 35.2 | $-641.08 | -7.6% | $358.92 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3879 | 50.8 | 49.9 | $-1032.36 | -2.7% | $-32.36 | -1.6 | done | can't tell from luck |
| value_ev10 | 1990 | 38.2 | 39.0 | $-1172.06 | -5.9% | $-172.06 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 3242 | 51.1 | 50.9 | $-1436.36 | -4.4% | $-436.36 | -2.6 | done | losing for real |
| value_ev5 | 2972 | 40.2 | 41.0 | $-1684.76 | -5.7% | $-684.76 | -2.6 | done | losing for real |
| momentum_60m_0.30pct | 3242 | 48.9 | 49.2 | $-1822.51 | -5.6% | $-822.51 | -3.2 | done | losing for real |
| trend_filter | 2311 | 48.3 | 50.4 | $-2124.17 | -9.2% | $-1124.17 | -4.5 | done | losing for real |
| momentum_15m_0.10pct | 3879 | 49.2 | 50.2 | $-2354.50 | -6.1% | $-1354.50 | -3.8 | done | losing for real |
| coinflip | 5711 | 49.9 | 49.9 | $-2510.23 | -4.4% | $-1510.23 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 5711 | 50.2 | 51.3 | $-3499.01 | -6.1% | $-2499.01 | -4.8 | done | losing for real |
| always_up | 5711 | 48.3 | 49.0 | $-3552.66 | -6.2% | $-2552.66 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10648 | 47.9 | 48.5 | $-6099.24 |
| ETH | 11532 | 47.9 | 47.6 | $-6146.23 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
