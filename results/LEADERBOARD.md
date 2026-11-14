# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 2:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 360 windows, 9718 settled trades, 46 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 186 | 37.1 | 36.6 | $-58.35 | -3.1% | $941.65 | -0.3 | Sat 9:15 PM | too few trades (186/200) |
| value_ev10 | 467 | 40.0 | 40.4 | $-211.62 | -4.5% | $788.38 | -0.8 | done | can't tell from luck |
| value_ev5 | 695 | 41.6 | 42.1 | $-353.12 | -5.1% | $646.88 | -1.2 | done | can't tell from luck |
| reversal_15m_0.10pct | 962 | 52.1 | 52.0 | $-396.07 | -4.1% | $603.93 | -1.3 | done | can't tell from luck |
| trend_filter | 538 | 48.5 | 50.5 | $-450.88 | -8.4% | $549.12 | -2.0 | done | can't tell from luck |
| reversal_60m_0.30pct | 803 | 51.1 | 52.0 | $-457.12 | -5.7% | $542.88 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 803 | 48.9 | 49.7 | $-483.76 | -6.0% | $516.24 | -1.7 | done | can't tell from luck |
| momentum_15m_0.10pct | 962 | 47.9 | 49.8 | $-741.87 | -7.7% | $258.13 | -2.4 | done | losing for real |
| coinflip | 1434 | 50.1 | 50.8 | $-742.65 | -5.2% | $257.35 | -2.0 | done | losing for real |
| momentum_5m_0.00pct | 1434 | 49.6 | 51.5 | $-1065.82 | -7.4% | $-65.82 | -2.9 | done | losing for real |
| always_up | 1434 | 46.2 | 50.6 | $-1772.59 | -12.4% | $-772.59 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2176 | 47.3 | 49.3 | $-1765.17 |
| ETH | 2449 | 47.7 | 48.8 | $-1757.44 |
| SOL | 2516 | 48.1 | 49.4 | $-1867.98 |
| XRP | 2577 | 48.8 | 49.2 | $-1343.26 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
