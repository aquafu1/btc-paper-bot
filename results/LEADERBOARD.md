# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 1:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 260 windows, 6823 settled trades, 47 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 677 | 55.7 | 52.2 | $+174.81 | +2.6% | $1174.81 | +0.7 | done | can't tell from luck |
| reversal_60m_0.30pct | 546 | 53.3 | 52.1 | $-103.93 | -1.9% | $896.07 | -0.5 | done | can't tell from luck |
| value_ev20 | 120 | 33.3 | 36.7 | $-151.51 | -12.6% | $848.49 | -1.1 | Sun 11:15 AM | too few trades (120/200) |
| value_ev10 | 324 | 36.4 | 40.7 | $-449.85 | -13.9% | $550.15 | -2.1 | done | losing for real |
| trend_filter | 358 | 45.5 | 50.4 | $-505.04 | -14.1% | $494.96 | -2.7 | done | losing for real |
| value_ev5 | 479 | 39.2 | 42.4 | $-550.76 | -11.5% | $449.24 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 546 | 46.7 | 49.8 | $-609.82 | -11.2% | $390.18 | -2.7 | done | losing for real |
| coinflip | 1032 | 49.2 | 50.8 | $-798.16 | -7.7% | $201.84 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 1032 | 49.3 | 51.5 | $-891.44 | -8.6% | $108.56 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 677 | 44.3 | 49.8 | $-1024.75 | -15.1% | $-24.75 | -4.0 | done | losing for real |
| always_up | 1032 | 47.3 | 50.2 | $-1064.64 | -10.3% | $-64.64 | -3.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1525 | 46.3 | 49.6 | $-1685.93 |
| ETH | 1698 | 46.6 | 49.1 | $-1791.01 |
| SOL | 1768 | 48.0 | 49.3 | $-1499.25 |
| XRP | 1832 | 48.7 | 49.2 | $-998.88 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
