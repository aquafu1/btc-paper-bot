# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 12:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 305 windows, 8153 settled trades, 49 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 152 | 34.9 | 36.5 | $-150.14 | -9.9% | $849.86 | -1.0 | Sun 1:30 AM | too few trades (152/200) |
| reversal_15m_0.10pct | 807 | 53.2 | 51.9 | $-160.43 | -2.0% | $839.57 | -0.6 | done | can't tell from luck |
| reversal_60m_0.30pct | 664 | 52.7 | 51.7 | $-173.75 | -2.6% | $826.25 | -0.7 | done | can't tell from luck |
| value_ev10 | 393 | 38.4 | 40.5 | $-366.52 | -9.3% | $633.48 | -1.6 | done | can't tell from luck |
| value_ev5 | 581 | 39.8 | 42.2 | $-587.82 | -10.1% | $412.18 | -2.2 | done | losing for real |
| trend_filter | 449 | 45.7 | 50.3 | $-616.14 | -13.7% | $383.86 | -3.0 | done | losing for real |
| momentum_60m_0.30pct | 664 | 47.3 | 49.9 | $-675.35 | -10.2% | $324.65 | -2.7 | done | losing for real |
| coinflip | 1212 | 50.1 | 50.9 | $-713.69 | -5.9% | $286.31 | -2.1 | done | losing for real |
| momentum_15m_0.10pct | 807 | 46.8 | 49.9 | $-826.14 | -10.2% | $173.86 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 1212 | 48.8 | 51.3 | $-1096.65 | -9.0% | $-96.65 | -3.3 | done | losing for real |
| always_up | 1212 | 47.4 | 50.4 | $-1222.34 | -10.1% | $-222.34 | -3.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1833 | 46.5 | 49.3 | $-1797.17 |
| ETH | 2039 | 47.2 | 48.8 | $-1862.60 |
| SOL | 2114 | 48.2 | 49.4 | $-1680.93 |
| XRP | 2167 | 48.5 | 49.1 | $-1248.25 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
