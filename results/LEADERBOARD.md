# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 3:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 364 windows, 9814 settled trades, 64 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 189 | 38.1 | 36.4 | $+15.78 | +0.8% | $1015.78 | +0.1 | Sat 8:30 PM | too few trades (189/200) |
| value_ev10 | 477 | 41.3 | 40.3 | $-42.64 | -0.9% | $957.36 | -0.2 | done | can't tell from luck |
| value_ev5 | 706 | 42.5 | 42.0 | $-168.96 | -2.4% | $831.04 | -0.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 973 | 51.9 | 52.0 | $-421.61 | -4.3% | $578.39 | -1.4 | done | can't tell from luck |
| momentum_60m_0.30pct | 805 | 49.1 | 49.8 | $-468.91 | -5.8% | $531.09 | -1.7 | done | can't tell from luck |
| trend_filter | 542 | 48.3 | 50.6 | $-475.35 | -8.8% | $524.65 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 805 | 50.9 | 52.0 | $-477.12 | -5.9% | $522.88 | -1.8 | done | can't tell from luck |
| momentum_15m_0.10pct | 973 | 48.1 | 49.6 | $-656.35 | -6.7% | $343.65 | -2.1 | done | losing for real |
| coinflip | 1448 | 50.1 | 50.8 | $-713.69 | -4.9% | $286.31 | -1.9 | done | can't tell from luck |
| momentum_5m_0.00pct | 1448 | 49.4 | 51.6 | $-1116.90 | -7.7% | $-116.90 | -3.0 | done | losing for real |
| always_up | 1448 | 45.9 | 50.7 | $-1887.41 | -13.0% | $-887.41 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2201 | 47.3 | 49.3 | $-1744.19 |
| ETH | 2468 | 47.7 | 48.8 | $-1710.76 |
| SOL | 2545 | 48.1 | 49.4 | $-1753.12 |
| XRP | 2600 | 48.9 | 49.1 | $-1205.10 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
