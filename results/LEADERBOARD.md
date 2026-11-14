# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 7:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 287 windows, 7589 settled trades, 48 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 748 | 54.3 | 51.7 | $+29.24 | +0.4% | $1029.24 | +0.1 | done | can't tell from luck |
| value_ev20 | 140 | 35.0 | 36.4 | $-129.35 | -9.2% | $870.65 | -0.9 | Sun 4:15 AM | too few trades (140/200) |
| reversal_60m_0.30pct | 610 | 52.3 | 51.8 | $-209.74 | -3.4% | $790.26 | -0.9 | done | can't tell from luck |
| value_ev10 | 367 | 38.1 | 40.5 | $-365.03 | -9.9% | $634.97 | -1.6 | done | can't tell from luck |
| trend_filter | 404 | 46.8 | 50.4 | $-476.66 | -11.8% | $523.34 | -2.4 | done | losing for real |
| value_ev5 | 542 | 39.9 | 42.2 | $-533.56 | -9.8% | $466.44 | -2.0 | done | losing for real |
| momentum_60m_0.30pct | 610 | 47.7 | 49.8 | $-557.45 | -9.1% | $442.55 | -2.3 | done | losing for real |
| coinflip | 1140 | 50.1 | 50.9 | $-666.80 | -5.8% | $333.20 | -2.0 | done | losing for real |
| momentum_5m_0.00pct | 1140 | 49.6 | 51.5 | $-896.16 | -7.9% | $103.84 | -2.8 | done | losing for real |
| momentum_15m_0.10pct | 748 | 45.7 | 50.0 | $-940.80 | -12.6% | $59.20 | -3.5 | done | losing for real |
| always_up | 1140 | 47.5 | 50.2 | $-1093.40 | -9.6% | $-93.40 | -3.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1688 | 46.8 | 49.4 | $-1574.85 |
| ETH | 1895 | 47.2 | 48.8 | $-1720.83 |
| SOL | 1973 | 48.3 | 49.3 | $-1525.15 |
| XRP | 2033 | 48.8 | 49.0 | $-1018.88 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
