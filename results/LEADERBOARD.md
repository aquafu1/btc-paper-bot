# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 8:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 107 windows, 2740 settled trades, 52 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 209 | 59.3 | 53.2 | $+185.81 | +8.9% | $1185.81 | +1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 265 | 55.5 | 52.0 | $+111.48 | +4.2% | $1111.48 | +0.7 | done | can't tell from luck |
| momentum_5m_0.00pct | 420 | 52.6 | 50.8 | $-18.65 | -0.4% | $981.35 | -0.1 | done | can't tell from luck |
| value_ev20 | 50 | 28.0 | 36.5 | $-123.85 | -24.8% | $876.15 | -1.4 | Sun 10:15 AM | too few trades (50/200) |
| value_ev10 | 142 | 38.7 | 40.6 | $-127.84 | -9.0% | $872.16 | -0.9 | Thu 7:45 AM | too few trades (142/200) |
| trend_filter | 144 | 42.4 | 49.0 | $-238.60 | -16.6% | $761.40 | -2.0 | Thu 7:15 AM | too few trades (144/200) |
| coinflip | 420 | 50.0 | 51.3 | $-274.24 | -6.5% | $725.76 | -1.4 | done | can't tell from luck |
| value_ev5 | 196 | 36.7 | 41.9 | $-310.08 | -15.8% | $689.92 | -2.0 | Wed 8:45 PM | too few trades (196/200) |
| momentum_15m_0.10pct | 265 | 44.5 | 50.1 | $-378.09 | -14.3% | $621.91 | -2.4 | done | losing for real |
| momentum_60m_0.30pct | 209 | 40.7 | 48.9 | $-409.02 | -19.6% | $590.98 | -2.8 | done | losing for real |
| always_up | 420 | 46.7 | 50.3 | $-463.36 | -11.0% | $536.64 | -2.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 593 | 45.5 | 49.7 | $-563.11 |
| ETH | 667 | 45.6 | 48.9 | $-649.58 |
| SOL | 732 | 48.4 | 48.6 | $-491.91 |
| XRP | 748 | 50.1 | 49.2 | $-341.84 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
