# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 10:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 251 windows, 6583 settled trades, 49 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 653 | 55.9 | 52.3 | $+178.15 | +2.7% | $1178.15 | +0.7 | done | can't tell from luck |
| reversal_60m_0.30pct | 525 | 53.3 | 52.1 | $-96.44 | -1.8% | $903.56 | -0.4 | done | can't tell from luck |
| value_ev20 | 116 | 33.6 | 36.7 | $-140.27 | -12.1% | $859.73 | -1.0 | Sun 11:15 AM | too few trades (116/200) |
| value_ev10 | 314 | 36.6 | 40.8 | $-433.26 | -13.8% | $566.74 | -2.1 | done | losing for real |
| trend_filter | 346 | 46.2 | 50.5 | $-435.88 | -12.6% | $564.12 | -2.4 | done | losing for real |
| value_ev5 | 463 | 38.9 | 42.5 | $-585.11 | -12.6% | $414.89 | -2.4 | done | losing for real |
| momentum_60m_0.30pct | 525 | 46.7 | 50.0 | $-599.00 | -11.4% | $401.00 | -2.7 | done | losing for real |
| momentum_5m_0.00pct | 996 | 50.1 | 51.6 | $-716.70 | -7.2% | $283.30 | -2.4 | done | losing for real |
| coinflip | 996 | 49.3 | 50.9 | $-770.68 | -7.7% | $229.32 | -2.5 | done | losing for real |
| momentum_15m_0.10pct | 653 | 44.1 | 49.9 | $-1019.42 | -15.6% | $-19.42 | -4.1 | done | losing for real |
| always_up | 996 | 46.8 | 50.5 | $-1174.84 | -11.8% | $-174.84 | -3.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1473 | 46.4 | 49.8 | $-1585.20 |
| ETH | 1643 | 46.7 | 49.1 | $-1722.35 |
| SOL | 1706 | 48.1 | 49.4 | $-1447.28 |
| XRP | 1761 | 48.6 | 49.2 | $-1038.64 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
