# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 26, 8:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1488 windows, 37286 settled trades, 336 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 756 | 34.3 | 35.4 | $-593.12 | -7.8% | $406.88 | -1.7 | done | can't tell from luck |
| value_ev10 | 1817 | 38.5 | 39.2 | $-975.06 | -5.4% | $24.94 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 3710 | 50.9 | 50.1 | $-1010.10 | -2.7% | $-10.10 | -1.7 | done | can't tell from luck |
| value_ev5 | 2740 | 40.4 | 41.1 | $-1424.76 | -5.2% | $-424.76 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 3119 | 51.0 | 51.0 | $-1497.24 | -4.8% | $-497.24 | -2.7 | done | losing for real |
| momentum_60m_0.30pct | 3119 | 49.0 | 49.2 | $-1636.15 | -5.2% | $-636.15 | -2.9 | done | losing for real |
| trend_filter | 2214 | 48.5 | 50.3 | $-1943.26 | -8.8% | $-943.26 | -4.2 | done | losing for real |
| momentum_15m_0.10pct | 3710 | 49.1 | 50.2 | $-2278.03 | -6.1% | $-1278.03 | -3.8 | done | losing for real |
| coinflip | 5367 | 50.0 | 50.0 | $-2383.92 | -4.4% | $-1383.92 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 5367 | 50.1 | 51.3 | $-3401.67 | -6.3% | $-2401.67 | -4.8 | done | losing for real |
| always_up | 5367 | 48.0 | 49.2 | $-3571.83 | -6.7% | $-2571.83 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9627 | 48.0 | 48.7 | $-5324.70 |
| ETH | 10349 | 47.9 | 47.9 | $-5806.21 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
