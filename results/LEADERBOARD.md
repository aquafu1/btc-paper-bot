# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 4:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1043 windows, 28944 settled trades, 54 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 541 | 34.6 | 35.1 | $-305.47 | -5.6% | $694.53 | -1.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 2938 | 51.2 | 50.5 | $-793.98 | -2.7% | $206.02 | -1.5 | done | can't tell from luck |
| value_ev10 | 1338 | 37.4 | 39.2 | $-1031.50 | -7.7% | $-31.50 | -2.3 | done | losing for real |
| momentum_60m_0.30pct | 2472 | 49.7 | 49.6 | $-1147.09 | -4.6% | $-147.09 | -2.3 | done | losing for real |
| trend_filter | 1727 | 49.3 | 50.7 | $-1356.95 | -7.9% | $-356.95 | -3.4 | done | losing for real |
| value_ev5 | 2026 | 39.3 | 41.0 | $-1469.33 | -7.3% | $-469.33 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 2472 | 50.3 | 51.0 | $-1586.09 | -6.4% | $-586.09 | -3.3 | done | losing for real |
| coinflip | 4164 | 50.5 | 50.3 | $-1707.15 | -4.1% | $-707.15 | -2.7 | done | losing for real |
| momentum_15m_0.10pct | 2938 | 48.8 | 50.3 | $-2055.14 | -7.0% | $-1055.14 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 4164 | 50.8 | 51.5 | $-2259.16 | -5.4% | $-1259.16 | -3.6 | done | losing for real |
| always_up | 4164 | 47.3 | 49.4 | $-3625.97 | -8.7% | $-2625.97 | -5.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6598 | 48.3 | 49.0 | $-3542.30 |
| ETH | 7167 | 48.1 | 48.5 | $-4490.88 |
| SOL | 7559 | 48.1 | 48.5 | $-4497.42 |
| XRP | 7620 | 48.1 | 48.3 | $-4807.21 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
