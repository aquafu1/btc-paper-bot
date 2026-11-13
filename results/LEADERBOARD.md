# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 11:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 255 windows, 6704 settled trades, 33 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 665 | 55.2 | 52.3 | $+97.72 | +1.5% | $1097.72 | +0.4 | done | can't tell from luck |
| reversal_60m_0.30pct | 534 | 53.2 | 52.0 | $-93.79 | -1.8% | $906.21 | -0.4 | done | can't tell from luck |
| value_ev20 | 119 | 33.6 | 36.7 | $-141.51 | -11.9% | $858.49 | -1.0 | Sun 10:30 AM | too few trades (119/200) |
| trend_filter | 351 | 46.4 | 50.7 | $-435.04 | -12.4% | $564.96 | -2.4 | done | losing for real |
| value_ev10 | 318 | 36.5 | 40.8 | $-444.49 | -14.0% | $555.51 | -2.1 | done | losing for real |
| value_ev5 | 470 | 39.1 | 42.4 | $-556.12 | -11.8% | $443.88 | -2.3 | done | losing for real |
| momentum_60m_0.30pct | 534 | 46.8 | 50.1 | $-598.95 | -11.2% | $401.05 | -2.7 | done | losing for real |
| momentum_5m_0.00pct | 1016 | 50.0 | 51.6 | $-745.81 | -7.3% | $254.19 | -2.4 | done | losing for real |
| coinflip | 1016 | 49.4 | 50.9 | $-749.00 | -7.4% | $251.00 | -2.4 | done | losing for real |
| momentum_15m_0.10pct | 665 | 44.8 | 49.9 | $-935.56 | -14.1% | $64.44 | -3.7 | done | losing for real |
| always_up | 1016 | 47.3 | 50.4 | $-1054.34 | -10.4% | $-54.34 | -3.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1496 | 46.7 | 49.7 | $-1514.77 |
| ETH | 1669 | 46.7 | 49.2 | $-1713.59 |
| SOL | 1737 | 48.1 | 49.4 | $-1456.91 |
| XRP | 1802 | 48.8 | 49.2 | $-971.62 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
