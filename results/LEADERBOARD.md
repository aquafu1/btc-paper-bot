# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 8:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 291 windows, 7700 settled trades, 76 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 760 | 53.8 | 51.9 | $-42.62 | -0.6% | $957.38 | -0.2 | done | can't tell from luck |
| value_ev20 | 143 | 36.4 | 36.4 | $-84.69 | -5.9% | $915.31 | -0.6 | Sun 3:30 AM | too few trades (143/200) |
| reversal_60m_0.30pct | 618 | 51.9 | 51.8 | $-250.58 | -4.1% | $749.42 | -1.1 | done | can't tell from luck |
| value_ev10 | 373 | 38.9 | 40.5 | $-303.14 | -8.1% | $696.86 | -1.3 | done | can't tell from luck |
| trend_filter | 412 | 47.3 | 50.3 | $-421.97 | -10.2% | $578.03 | -2.1 | done | losing for real |
| value_ev5 | 548 | 40.3 | 42.1 | $-471.67 | -8.6% | $528.33 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 618 | 48.1 | 49.8 | $-510.68 | -8.3% | $489.32 | -2.1 | done | losing for real |
| coinflip | 1156 | 50.2 | 50.9 | $-639.26 | -5.5% | $360.74 | -1.9 | done | can't tell from luck |
| momentum_5m_0.00pct | 1156 | 49.7 | 51.4 | $-849.38 | -7.3% | $150.62 | -2.6 | done | losing for real |
| momentum_15m_0.10pct | 760 | 46.2 | 49.8 | $-854.03 | -11.2% | $145.97 | -3.1 | done | losing for real |
| always_up | 1156 | 47.2 | 50.2 | $-1166.10 | -10.1% | $-166.10 | -3.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1714 | 47.0 | 49.4 | $-1481.43 |
| ETH | 1922 | 47.4 | 48.7 | $-1617.16 |
| SOL | 2004 | 48.4 | 49.3 | $-1490.95 |
| XRP | 2060 | 48.8 | 49.0 | $-1004.59 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
