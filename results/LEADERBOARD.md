# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 12:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 259 windows, 6796 settled trades, 51 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 676 | 55.6 | 52.2 | $+159.47 | +2.4% | $1159.47 | +0.6 | done | can't tell from luck |
| reversal_60m_0.30pct | 545 | 53.2 | 52.1 | $-109.39 | -2.0% | $890.61 | -0.5 | done | can't tell from luck |
| value_ev20 | 119 | 33.6 | 36.7 | $-141.51 | -11.9% | $858.49 | -1.0 | Sun 11:45 AM | too few trades (119/200) |
| value_ev10 | 320 | 36.6 | 40.7 | $-435.19 | -13.6% | $564.81 | -2.1 | done | losing for real |
| trend_filter | 356 | 45.8 | 50.5 | $-485.04 | -13.6% | $514.96 | -2.6 | done | losing for real |
| value_ev5 | 475 | 39.4 | 42.4 | $-536.10 | -11.3% | $463.90 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 545 | 46.8 | 49.9 | $-599.82 | -11.0% | $400.18 | -2.6 | done | losing for real |
| coinflip | 1028 | 49.3 | 50.8 | $-773.62 | -7.5% | $226.38 | -2.5 | done | losing for real |
| momentum_5m_0.00pct | 1028 | 49.5 | 51.6 | $-851.44 | -8.3% | $148.56 | -2.8 | done | losing for real |
| momentum_15m_0.10pct | 676 | 44.4 | 49.8 | $-1014.75 | -15.0% | $-14.75 | -4.0 | done | losing for real |
| always_up | 1028 | 47.4 | 50.3 | $-1049.99 | -10.2% | $-49.99 | -3.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1519 | 46.5 | 49.6 | $-1625.93 |
| ETH | 1690 | 46.7 | 49.1 | $-1741.93 |
| SOL | 1762 | 48.1 | 49.3 | $-1439.25 |
| XRP | 1825 | 48.7 | 49.2 | $-1030.26 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
