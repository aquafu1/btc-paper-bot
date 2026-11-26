# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 26, 7:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1485 windows, 37257 settled trades, 337 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 755 | 34.3 | 35.4 | $-583.12 | -7.7% | $416.88 | -1.6 | done | can't tell from luck |
| value_ev10 | 1816 | 38.5 | 39.2 | $-965.06 | -5.3% | $34.94 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3709 | 50.9 | 50.1 | $-1000.10 | -2.7% | $-0.10 | -1.6 | done | can't tell from luck |
| value_ev5 | 2738 | 40.4 | 41.1 | $-1426.86 | -5.2% | $-426.86 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 3117 | 51.0 | 51.0 | $-1490.54 | -4.8% | $-490.54 | -2.7 | done | losing for real |
| momentum_60m_0.30pct | 3117 | 49.0 | 49.2 | $-1636.03 | -5.2% | $-636.03 | -2.9 | done | losing for real |
| trend_filter | 2213 | 48.5 | 50.3 | $-1953.15 | -8.8% | $-953.15 | -4.2 | done | losing for real |
| momentum_15m_0.10pct | 3709 | 49.1 | 50.2 | $-2290.13 | -6.2% | $-1290.13 | -3.8 | done | losing for real |
| coinflip | 5361 | 49.9 | 50.0 | $-2396.18 | -4.5% | $-1396.18 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 5361 | 50.1 | 51.3 | $-3414.92 | -6.4% | $-2414.92 | -4.8 | done | losing for real |
| always_up | 5361 | 48.1 | 49.2 | $-3550.14 | -6.6% | $-2550.14 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9618 | 48.0 | 48.7 | $-5351.10 |
| ETH | 10329 | 47.9 | 48.0 | $-5770.90 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
