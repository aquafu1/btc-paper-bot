# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 12:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 787 windows, 21708 settled trades, 26 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 404 | 32.9 | 34.9 | $-391.45 | -9.7% | $608.55 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 1838 | 50.2 | 49.6 | $-685.16 | -3.7% | $314.84 | -1.6 | done | can't tell from luck |
| trend_filter | 1277 | 50.4 | 50.8 | $-709.41 | -5.6% | $290.59 | -2.0 | done | losing for real |
| value_ev10 | 989 | 37.4 | 39.1 | $-778.33 | -7.9% | $221.67 | -2.0 | done | losing for real |
| reversal_15m_0.10pct | 2217 | 50.9 | 50.6 | $-813.18 | -3.7% | $186.82 | -1.7 | done | can't tell from luck |
| value_ev5 | 1496 | 39.8 | 41.1 | $-1006.66 | -6.7% | $-6.66 | -2.2 | done | losing for real |
| coinflip | 3144 | 50.3 | 50.3 | $-1310.91 | -4.2% | $-310.91 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1838 | 49.8 | 51.2 | $-1352.25 | -7.4% | $-352.25 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 2217 | 49.1 | 50.2 | $-1371.81 | -6.2% | $-371.81 | -2.9 | done | losing for real |
| momentum_5m_0.00pct | 3144 | 51.3 | 51.7 | $-1424.06 | -4.5% | $-424.06 | -2.6 | done | losing for real |
| always_up | 3144 | 47.6 | 49.6 | $-2641.72 | -8.4% | $-1641.72 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4930 | 48.3 | 49.1 | $-2937.84 |
| ETH | 5412 | 48.1 | 48.5 | $-3535.47 |
| SOL | 5656 | 48.3 | 48.6 | $-3145.93 |
| XRP | 5710 | 48.5 | 48.5 | $-2865.69 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
