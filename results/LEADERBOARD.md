# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 11:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 253 windows, 6632 settled trades, 48 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 657 | 55.9 | 52.2 | $+177.72 | +2.7% | $1177.72 | +0.7 | done | can't tell from luck |
| reversal_60m_0.30pct | 528 | 53.2 | 52.1 | $-111.36 | -2.1% | $888.64 | -0.5 | done | can't tell from luck |
| value_ev20 | 118 | 33.1 | 36.7 | $-160.27 | -13.6% | $839.73 | -1.2 | Sun 10:15 AM | too few trades (118/200) |
| trend_filter | 347 | 46.4 | 50.6 | $-430.99 | -12.4% | $569.01 | -2.4 | done | losing for real |
| value_ev10 | 317 | 36.3 | 40.8 | $-463.26 | -14.6% | $536.74 | -2.2 | done | losing for real |
| value_ev5 | 468 | 38.9 | 42.5 | $-590.71 | -12.6% | $409.29 | -2.4 | done | losing for real |
| momentum_60m_0.30pct | 528 | 46.8 | 50.0 | $-593.84 | -11.2% | $406.16 | -2.7 | done | losing for real |
| momentum_5m_0.00pct | 1004 | 50.0 | 51.6 | $-745.71 | -7.4% | $254.29 | -2.5 | done | losing for real |
| coinflip | 1004 | 49.4 | 50.9 | $-760.45 | -7.6% | $239.55 | -2.5 | done | losing for real |
| momentum_15m_0.10pct | 657 | 44.1 | 49.9 | $-1021.15 | -15.5% | $-21.15 | -4.1 | done | losing for real |
| always_up | 1004 | 46.8 | 50.4 | $-1170.87 | -11.7% | $-170.87 | -3.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1486 | 46.5 | 49.8 | $-1576.41 |
| ETH | 1653 | 46.6 | 49.1 | $-1745.11 |
| SOL | 1717 | 48.0 | 49.4 | $-1504.37 |
| XRP | 1776 | 48.6 | 49.2 | $-1045.01 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
