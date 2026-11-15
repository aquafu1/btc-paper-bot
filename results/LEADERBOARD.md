# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 2:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 411 windows, 11282 settled trades, 45 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 203 | 36.0 | 36.5 | $-96.95 | -4.8% | $903.05 | -0.5 | done | can't tell from luck |
| value_ev10 | 529 | 40.3 | 40.5 | $-211.49 | -4.0% | $788.51 | -0.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 964 | 50.8 | 50.0 | $-234.67 | -2.4% | $765.33 | -0.8 | done | can't tell from luck |
| value_ev5 | 796 | 42.1 | 42.2 | $-311.69 | -3.9% | $688.31 | -1.0 | done | can't tell from luck |
| trend_filter | 640 | 49.8 | 50.7 | $-350.74 | -5.5% | $649.26 | -1.4 | done | can't tell from luck |
| momentum_15m_0.10pct | 1136 | 49.2 | 49.9 | $-551.36 | -4.9% | $448.64 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 1136 | 50.8 | 51.9 | $-689.87 | -6.1% | $310.13 | -2.2 | done | losing for real |
| coinflip | 1638 | 50.2 | 51.0 | $-802.72 | -4.9% | $197.28 | -2.0 | done | losing for real |
| reversal_60m_0.30pct | 964 | 49.2 | 51.9 | $-868.50 | -9.0% | $131.50 | -2.9 | done | losing for real |
| momentum_5m_0.00pct | 1638 | 49.7 | 51.6 | $-1149.35 | -7.0% | $-149.35 | -2.9 | done | losing for real |
| always_up | 1638 | 45.8 | 50.6 | $-2126.22 | -13.0% | $-1126.22 | -5.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2546 | 47.6 | 49.5 | $-1842.64 |
| ETH | 2839 | 48.0 | 49.0 | $-1717.01 |
| SOL | 2925 | 47.8 | 49.5 | $-2306.13 |
| XRP | 2972 | 48.9 | 49.3 | $-1527.78 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
