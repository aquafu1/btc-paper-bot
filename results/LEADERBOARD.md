# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 10:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1258 windows, 34021 settled trades, 420 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 665 | 34.1 | 35.3 | $-524.16 | -7.9% | $475.84 | -1.6 | done | can't tell from luck |
| value_ev10 | 1629 | 38.4 | 39.2 | $-908.07 | -5.6% | $91.93 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3411 | 50.7 | 50.3 | $-1157.75 | -3.4% | $-157.75 | -2.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 2855 | 49.6 | 49.4 | $-1259.83 | -4.4% | $-259.83 | -2.4 | done | losing for real |
| value_ev5 | 2462 | 40.3 | 41.1 | $-1357.52 | -5.5% | $-357.52 | -2.3 | done | losing for real |
| trend_filter | 2015 | 48.9 | 50.4 | $-1627.97 | -8.1% | $-627.97 | -3.7 | done | losing for real |
| reversal_60m_0.30pct | 2855 | 50.4 | 51.1 | $-1731.69 | -6.1% | $-731.69 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 3411 | 49.3 | 50.2 | $-2060.11 | -6.0% | $-1060.11 | -3.6 | done | losing for real |
| coinflip | 4906 | 50.1 | 50.1 | $-2178.13 | -4.4% | $-1178.13 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 4906 | 50.4 | 51.4 | $-2866.64 | -5.8% | $-1866.64 | -4.2 | done | losing for real |
| always_up | 4906 | 47.8 | 49.4 | $-3629.39 | -7.4% | $-2629.39 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8036 | 48.0 | 48.9 | $-4703.46 |
| ETH | 8675 | 48.1 | 48.3 | $-5013.56 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
