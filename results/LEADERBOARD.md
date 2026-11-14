# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 1:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 311 windows, 8307 settled trades, 63 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 822 | 53.2 | 51.8 | $-134.75 | -1.6% | $865.25 | -0.5 | done | can't tell from luck |
| reversal_60m_0.30pct | 676 | 52.7 | 51.7 | $-161.55 | -2.4% | $838.45 | -0.6 | done | can't tell from luck |
| value_ev20 | 155 | 34.2 | 36.6 | $-180.14 | -11.6% | $819.86 | -1.1 | Sun 1:30 AM | too few trades (155/200) |
| value_ev10 | 398 | 37.9 | 40.5 | $-416.52 | -10.5% | $583.48 | -1.8 | done | can't tell from luck |
| trend_filter | 457 | 45.7 | 50.4 | $-622.41 | -13.6% | $377.59 | -3.0 | done | losing for real |
| value_ev5 | 593 | 39.5 | 42.2 | $-634.15 | -10.7% | $365.85 | -2.3 | done | losing for real |
| momentum_60m_0.30pct | 676 | 47.3 | 50.0 | $-676.16 | -10.0% | $323.84 | -2.7 | done | losing for real |
| coinflip | 1236 | 49.9 | 50.9 | $-759.15 | -6.1% | $240.85 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 822 | 46.8 | 49.9 | $-845.92 | -10.3% | $154.08 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 1236 | 48.9 | 51.4 | $-1104.11 | -8.9% | $-104.11 | -3.3 | done | losing for real |
| always_up | 1236 | 47.2 | 50.4 | $-1280.35 | -10.4% | $-280.35 | -3.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1865 | 46.4 | 49.3 | $-1869.25 |
| ETH | 2079 | 47.0 | 48.8 | $-1954.19 |
| SOL | 2163 | 47.9 | 49.4 | $-1755.55 |
| XRP | 2200 | 48.6 | 49.1 | $-1236.21 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
