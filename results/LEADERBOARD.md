# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 4:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 417 windows, 11470 settled trades, 52 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 209 | 34.9 | 36.4 | $-156.95 | -7.5% | $843.05 | -0.8 | done | can't tell from luck |
| value_ev10 | 536 | 39.7 | 40.4 | $-281.49 | -5.3% | $718.51 | -1.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 984 | 50.6 | 50.1 | $-307.89 | -3.1% | $692.11 | -1.0 | done | can't tell from luck |
| value_ev5 | 805 | 41.7 | 42.1 | $-380.32 | -4.7% | $619.68 | -1.2 | done | can't tell from luck |
| trend_filter | 660 | 49.7 | 50.8 | $-402.59 | -6.1% | $597.41 | -1.6 | done | can't tell from luck |
| momentum_15m_0.10pct | 1156 | 49.6 | 50.0 | $-509.17 | -4.4% | $490.83 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 1156 | 50.4 | 51.8 | $-790.90 | -6.8% | $209.10 | -2.4 | done | losing for real |
| coinflip | 1660 | 50.2 | 50.9 | $-831.51 | -5.0% | $168.49 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 984 | 49.4 | 51.8 | $-855.63 | -8.7% | $144.37 | -2.9 | done | losing for real |
| momentum_5m_0.00pct | 1660 | 49.6 | 51.6 | $-1201.90 | -7.2% | $-201.90 | -3.1 | done | losing for real |
| always_up | 1660 | 45.7 | 50.6 | $-2198.07 | -13.2% | $-1198.07 | -5.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2596 | 47.7 | 49.4 | $-1905.65 |
| ETH | 2885 | 47.9 | 49.0 | $-1860.12 |
| SOL | 2971 | 47.6 | 49.5 | $-2505.25 |
| XRP | 3018 | 48.8 | 49.3 | $-1645.39 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
